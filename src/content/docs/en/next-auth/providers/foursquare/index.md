---
title: "Foursquare"
description: 'Foursquare requires an additional  parameter in  format, which essentially states "I''m prepared for API changes up to this date".'
---

Source URL: https://next-auth.js.org/providers/foursquare

# Foursquare | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/foursquare#documentation "Direct link to heading")

<https://developer.foursquare.com/docs/places-api/authentication/#web-applications>

## Configuration[​](https://next-auth.js.org/providers/foursquare#configuration "Direct link to heading")

<https://developer.foursquare.com/>

danger

Foursquare requires an additional `apiVersion` parameter in [`YYYYMMDD` format](https://developer.foursquare.com/docs/places-api/versioning/), which essentially states "I'm prepared for API changes up to this date".

## Options[​](https://next-auth.js.org/providers/foursquare#options "Direct link to heading")

The **Foursquare Provider** comes with a set of default options:

- [Foursquare Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/foursquare.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/foursquare#example "Direct link to heading")

```
    import FourSquareProvider from "next-auth/providers/foursquare";
    ...
    providers: [
      FourSquareProvider({
        clientId: process.env.FOURSQUARE_CLIENT_ID,
        clientSecret: process.env.FOURSQUARE_CLIENT_SECRET,
        apiVersion: "YYYYMMDD"
      })
    ]
    ...

```
