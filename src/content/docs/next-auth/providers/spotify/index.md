---
title: "Spotify"
description: "원본 URL: https://next-auth.js.org/providers/spotify"
---

원본 URL: https://next-auth.js.org/providers/spotify

# Spotify | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/spotify#documentation "헤딩으로 바로 가는 링크")

<https://developer.spotify.com/documentation/general/guides/authorization-guide>

## 구성[​](https://next-auth.js.org/providers/spotify#configuration "헤딩으로 바로 가는 링크")

<https://developer.spotify.com/dashboard/applications>

## 옵션[​](https://next-auth.js.org/providers/spotify#options "헤딩으로 바로 가는 링크")

**Spotify Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Spotify Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/spotify.ts)

사용 사례에 맞게 원하는 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/spotify#example "헤딩으로 바로 가는 링크")

```
    import SpotifyProvider from "next-auth/providers/spotify";
    ...
    providers: [
      SpotifyProvider({
        clientId: process.env.SPOTIFY_CLIENT_ID,
        clientSecret: process.env.SPOTIFY_CLIENT_SECRET
      })
    ]
    ...

```
