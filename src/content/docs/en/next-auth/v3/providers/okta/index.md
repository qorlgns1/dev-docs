---
title: "Okta"
description: "The Okta Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/okta

# Okta | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/okta#documentation "Direct link to heading")

<https://developer.okta.com/docs/reference/api/oidc>

## Options[​](https://next-auth.js.org/v3/providers/okta#options "Direct link to heading")

The **Okta Provider** comes with a set of default options:

- [Okta Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/okta.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/okta#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Okta({
        clientId: process.env.OKTA_CLIENT_ID,
        clientSecret: process.env.OKTA_CLIENT_SECRET,
        domain: process.env.OKTA_DOMAIN
      })
    ]
    ...

```
