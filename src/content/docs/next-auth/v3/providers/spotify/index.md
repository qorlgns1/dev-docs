---
title: "Spotify"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/spotify

# Spotify | NextAuth.js

Version: v3

## 문서[​](https://next-auth.js.org/v3/providers/spotify#documentation "Direct link to heading")

<https://developer.spotify.com/documentation>

## 구성[​](https://next-auth.js.org/v3/providers/spotify#configuration "Direct link to heading")

<https://developer.spotify.com/dashboard/applications>

## 옵션[​](https://next-auth.js.org/v3/providers/spotify#options "Direct link to heading")

**Spotify Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Spotify Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/spotify.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/spotify#example "Direct link to heading")

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
