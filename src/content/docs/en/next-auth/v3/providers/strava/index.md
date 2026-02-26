---
title: "Strava"
description: "The Strava Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/strava

# Strava | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/strava#documentation "Direct link to heading")

<http://developers.strava.com/docs/reference/>

## Options[​](https://next-auth.js.org/v3/providers/strava#options "Direct link to heading")

The **Strava Provider** comes with a set of default options:

- [Strava Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/strava.js)

You can override any of the options to suit your own use case. Ensure the `redirect_uri` configuration fits your needs accordingly.

## Example[​](https://next-auth.js.org/v3/providers/strava#example "Direct link to heading")

```
    import Providers from 'next-auth/providers'
    ...
    providers: [
      Providers.Strava({
        clientId: process.env.STRAVA_CLIENT_ID,
        clientSecret: process.env.STRAVA_CLIENT_SECRET,
      })
    ]
    ...

```
