---
title: "Keycloak"
description: 'Create an openid-connect client in Keycloak with "confidential" as the "Access Type".'
---

Source URL: https://next-auth.js.org/providers/keycloak

# Keycloak | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/keycloak#documentation "Direct link to heading")

<https://www.keycloak.org/docs/latest/server_admin/#_oidc_clients>

## Configuration[​](https://next-auth.js.org/providers/keycloak#configuration "Direct link to heading")

tip

Create an openid-connect client in Keycloak with "confidential" as the "Access Type".

## Options[​](https://next-auth.js.org/providers/keycloak#options "Direct link to heading")

The **Keycloak Provider** comes with a set of default options:

- [Keycloak Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/keycloak.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/keycloak#example "Direct link to heading")

```
    import KeycloakProvider from "next-auth/providers/keycloak";
    ...
    providers: [
      KeycloakProvider({
        clientId: process.env.KEYCLOAK_ID,
        clientSecret: process.env.KEYCLOAK_SECRET,
        issuer: process.env.KEYCLOAK_ISSUER,
      })
    ]
    ...

```

note

`issuer` should include the realm – e.g. `https://my-keycloak-domain.com/realms/My_Realm`
