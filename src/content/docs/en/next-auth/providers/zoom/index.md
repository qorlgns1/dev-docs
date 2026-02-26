---
title: "Zoom"
description: "The Zoom Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/zoom

# Zoom | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/zoom#documentation "Direct link to heading")

<https://marketplace.zoom.us/docs/guides/auth/oauth>

## Configuration[​](https://next-auth.js.org/providers/zoom#configuration "Direct link to heading")

<https://marketplace.zoom.us>

## Options[​](https://next-auth.js.org/providers/zoom#options "Direct link to heading")

The **Zoom Provider** comes with a set of default options:

- [Zoom Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/zoom.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/zoom#example "Direct link to heading")

```
    import ZoomProvider from "next-auth/providers/zoom"
    ...
    providers: [
      ZoomProvider({
        clientId: process.env.ZOOM_CLIENT_ID,
        clientSecret: process.env.ZOOM_CLIENT_SECRET
      })
    }
    ...

```
