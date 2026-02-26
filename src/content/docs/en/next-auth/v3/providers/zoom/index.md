---
title: "Zoom"
description: "The Zoom Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/zoom

# Zoom | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/zoom#documentation "Direct link to heading")

<https://marketplace.zoom.us/docs/guides/auth/oauth>

## Configuration[​](https://next-auth.js.org/v3/providers/zoom#configuration "Direct link to heading")

<https://marketplace.zoom.us>

## Options[​](https://next-auth.js.org/v3/providers/zoom#options "Direct link to heading")

The **Zoom Provider** comes with a set of default options:

- [Zoom Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/zoom.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/zoom#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Zoom({
        clientId: process.env.ZOOM_CLIENT_ID,
        clientSecret: process.env.ZOOM_CLIENT_SECRET
      })
    }
    ...

```
