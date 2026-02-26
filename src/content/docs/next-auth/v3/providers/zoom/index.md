---
title: "Zoom"
description: "사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/v3/providers/zoom

# Zoom | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/zoom#documentation "Direct link to heading")

<https://marketplace.zoom.us/docs/guides/auth/oauth>

## 구성[​](https://next-auth.js.org/v3/providers/zoom#configuration "Direct link to heading")

<https://marketplace.zoom.us>

## 옵션[​](https://next-auth.js.org/v3/providers/zoom#options "Direct link to heading")

**Zoom Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Zoom Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/zoom.js)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/zoom#example "Direct link to heading")

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
