---
title: "Zoom"
description: "자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/zoom

# Zoom | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/zoom#documentation "제목으로 가는 직접 링크")

<https://marketplace.zoom.us/docs/guides/auth/oauth>

## 구성[​](https://next-auth.js.org/providers/zoom#configuration "제목으로 가는 직접 링크")

<https://marketplace.zoom.us>

## 옵션[​](https://next-auth.js.org/providers/zoom#options "제목으로 가는 직접 링크")

**Zoom Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Zoom Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/zoom.ts)

자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/zoom#example "제목으로 가는 직접 링크")

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
