---
title: "Auth0"
description: "The Auth0 Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/auth0

# Auth0 | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/auth0#documentation "Direct link to heading")

<https://auth0.com/docs/api/authentication#authorize-application>

## Configuration[​](https://next-auth.js.org/providers/auth0#configuration "Direct link to heading")

<https://manage.auth0.com/dashboard>

## Options[​](https://next-auth.js.org/providers/auth0#options "Direct link to heading")

The **Auth0 Provider** comes with a set of default options:

- [Auth0 Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/auth0.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/auth0#example "Direct link to heading")

```
    import Auth0Provider from "next-auth/providers/auth0";
    ...
    providers: [
      Auth0Provider({
        clientId: process.env.AUTH0_CLIENT_ID,
        clientSecret: process.env.AUTH0_CLIENT_SECRET,
        issuer: process.env.AUTH0_ISSUER
      })
    ]
    ...

```

note

`issuer` should be the fully qualified URL – e.g. `https://dev-s6clz2lv.eu.auth0.com`
