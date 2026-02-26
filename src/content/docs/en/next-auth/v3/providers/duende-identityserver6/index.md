---
title: "DuendeIdentityServer6"
description: "The DuendeIdentityServer6 Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/duende-identityserver6

# DuendeIdentityServer6 | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/duende-identityserver6#documentation "Direct link to heading")

<https://docs.duendesoftware.com/identityserver/v6>

## Options[​](https://next-auth.js.org/v3/providers/duende-identityserver6#options "Direct link to heading")

The **DuendeIdentityServer6 Provider** comes with a set of default options:

- [DuendeIdentityServer6 Provider options](https://github.com/nextauthjs/next-auth/tree/main/packages/next-auth/src/providers/duende-identity-server6.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/duende-identityserver6#example "Direct link to heading")

```
    import DuendeIDS6Provider from "next-auth/providers/duende-identity-server6"

    ...
    providers: [
      DuendeIDS6Provider({
        clientId: process.env.DUENDE_IDS6_ID,
        clientSecret: process.env.DUENDE_IDS6_SECRET,
        issuer: process.env.DUENDE_IDS6_ISSUER,
      })
    ]
    ...

```

## Demo IdentityServer[​](https://next-auth.js.org/v3/providers/duende-identityserver6#demo-identityserver "Direct link to heading")

The configuration below is for the demo server at <https://demo.duendesoftware.com/>

If you want to try it out, you can copy and paste the configuration below.

You can sign in to the demo service with either **bob/bob** or **alice/alice**.

```
    import DuendeIDS6Provider from "next-auth/providers/duende-identity-server6"
    ...
    providers: [
      DuendeIDS6Provider({
        clientId: "interactive.confidential",
        clientSecret: "secret",
        issuer: "https://demo.duendesoftware.com",
      })
    ]
    ...

```
