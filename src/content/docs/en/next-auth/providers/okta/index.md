---
title: "Okta"
description: "The Okta Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/okta

# Okta | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/okta#documentation "Direct link to heading")

<https://developer.okta.com/docs/reference/api/oidc>

## Options[​](https://next-auth.js.org/providers/okta#options "Direct link to heading")

The **Okta Provider** comes with a set of default options:

- [Okta Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/okta.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/okta#example "Direct link to heading")

```
    import OktaProvider from "next-auth/providers/okta";
    ...
    providers: [
      OktaProvider({
        clientId: process.env.OKTA_CLIENT_ID,
        clientSecret: process.env.OKTA_CLIENT_SECRET,
        issuer: process.env.OKTA_ISSUER
      })
    ]
    ...

```
