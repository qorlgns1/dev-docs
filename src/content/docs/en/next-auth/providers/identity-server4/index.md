---
title: "IdentityServer4"
description: "The IdentityServer4 Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/identity-server4

# IdentityServer4 | NextAuth.js

Version: v4

danger

[IdentityServer4 is discontinued](https://identityserver4.readthedocs.io/en/latest/#:~:text=until%20November%202022.) and only releases security updates until November 2022. You should consider an alternative provider.

## Documentation[​](https://next-auth.js.org/providers/identity-server4#documentation "Direct link to heading")

<https://identityserver4.readthedocs.io/en/latest/>

## Options[​](https://next-auth.js.org/providers/identity-server4#options "Direct link to heading")

The **IdentityServer4 Provider** comes with a set of default options:

- [IdentityServer4 Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/identity-server4.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/identity-server4#example "Direct link to heading")

```
    import IdentityServer4Provider from "next-auth/providers/identity-server4";
    ...
    providers: [
      IdentityServer4Provider({
        id: "identity-server4",
        name: "IdentityServer4",
        issuer:  process.env.IdentityServer4_Issuer,
        clientId: process.env.IdentityServer4_CLIENT_ID,
        clientSecret: process.env.IdentityServer4_CLIENT_SECRET
      })
    ]
    ...

```
