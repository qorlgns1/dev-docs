---
title: "Auth0"
description: "Configure your application in Auth0 as a 'Regular Web Application' (not a 'Single Page App')."
---

Source URL: https://next-auth.js.org/v3/providers/auth0

# Auth0 | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/auth0#documentation "Direct link to heading")

<https://auth0.com/docs/api/authentication#authorize-application>

## Configuration[​](https://next-auth.js.org/v3/providers/auth0#configuration "Direct link to heading")

<https://manage.auth0.com/dashboard>

tip

Configure your application in Auth0 as a 'Regular Web Application' (not a 'Single Page App').

## Options[​](https://next-auth.js.org/v3/providers/auth0#options "Direct link to heading")

The **Auth0 Provider** comes with a set of default options:

- [Auth0 Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/auth0.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/auth0#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Auth0({
        clientId: process.env.AUTH0_CLIENT_ID,
        clientSecret: process.env.AUTH0_CLIENT_SECRET,
        domain: process.env.AUTH0_DOMAIN
      })
    ]
    ...

```

note

`domain` should be the fully qualified domain – e.g. `dev-s6clz2lv.eu.auth0.com`
