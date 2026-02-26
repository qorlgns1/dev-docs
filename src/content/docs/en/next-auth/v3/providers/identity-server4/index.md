---
title: "IdentityServer4"
description: "The IdentityServer4 Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/identity-server4

# IdentityServer4 | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/identity-server4#documentation "Direct link to heading")

<https://identityserver4.readthedocs.io/en/latest/>

## Options[​](https://next-auth.js.org/v3/providers/identity-server4#options "Direct link to heading")

The **IdentityServer4 Provider** comes with a set of default options:

- [IdentityServer4 Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/identity-server4.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/identity-server4#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.IdentityServer4({
        id: "identity-server4",
        name: "IdentityServer4",
        scope: "openid profile email api offline_access", // Allowed Scopes
        domain:  process.env.IdentityServer4_Domain,
        clientId: process.env.IdentityServer4_CLIENT_ID,
        clientSecret: process.env.IdentityServer4_CLIENT_SECRET
      })
    ]
    ...

```

## Demo IdentityServer[​](https://next-auth.js.org/v3/providers/identity-server4#demo-identityserver "Direct link to heading")

The configuration below is for the demo server at <https://demo.identityserver.io/>

If you want to try it out, you can copy and paste the configuration below.

You can sign in to the demo service with either **bob/bob** or **alice/alice**.

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.IdentityServer4({
        id: "demo-identity-server",
        name: "Demo IdentityServer4",
        scope: "openid profile email api offline_access",
        domain:  "demo.identityserver.io",
        clientId: "interactive.confidential",
        clientSecret: "secret",
        protection: "pkce"
      })
    ]
    ...

```
