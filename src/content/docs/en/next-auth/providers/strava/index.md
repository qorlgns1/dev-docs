---
title: "Strava"
description: "The Strava Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/strava

# Strava | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/strava#documentation "Direct link to heading")

<http://developers.strava.com/docs/reference/>

## Options[​](https://next-auth.js.org/providers/strava#options "Direct link to heading")

The **Strava Provider** comes with a set of default options:

- [Strava Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/strava.ts)

You can override any of the options to suit your own use case. Ensure the redirect_uri configuration fits your needs accordingly.

## Example[​](https://next-auth.js.org/providers/strava#example "Direct link to heading")

```
    import StravaProvider from "next-auth/providers/strava";
    ...
    providers: [
      StravaProvider({
        clientId: process.env.STRAVA_CLIENT_ID,
        clientSecret: process.env.STRAVA_CLIENT_SECRET,
      })
    ]
    ...

```
