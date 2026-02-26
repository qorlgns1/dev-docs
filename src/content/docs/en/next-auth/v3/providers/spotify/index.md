---
title: "Spotify"
description: "The Spotify Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/spotify

# Spotify | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/spotify#documentation "Direct link to heading")

<https://developer.spotify.com/documentation>

## Configuration[​](https://next-auth.js.org/v3/providers/spotify#configuration "Direct link to heading")

<https://developer.spotify.com/dashboard/applications>

## Options[​](https://next-auth.js.org/v3/providers/spotify#options "Direct link to heading")

The **Spotify Provider** comes with a set of default options:

- [Spotify Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/spotify.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/spotify#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Spotify({
        clientId: process.env.SPOTIFY_CLIENT_ID,
        clientSecret: process.env.SPOTIFY_CLIENT_SECRET
      })
    ]
    ...

```
