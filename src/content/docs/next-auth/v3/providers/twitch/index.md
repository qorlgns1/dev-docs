---
title: "Twitch"
description: "원본 URL: https://next-auth.js.org/v3/providers/twitch"
---

원본 URL: https://next-auth.js.org/v3/providers/twitch

# Twitch | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/twitch#documentation "제목으로 바로 가는 링크")

<https://dev.twitch.tv/docs/authentication>

## 설정[​](https://next-auth.js.org/v3/providers/twitch#configuration "제목으로 바로 가는 링크")

<https://dev.twitch.tv/console/apps>

콘솔에 다음 redirect URL을 추가하세요 `http://<your-next-app-url>/api/auth/callback/twitch`

## 옵션[​](https://next-auth.js.org/v3/providers/twitch#options "제목으로 바로 가는 링크")

**Twitch Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Twitch Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/twitch.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/twitch#example "제목으로 바로 가는 링크")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Twitch({
        clientId: process.env.TWITCH_CLIENT_ID,
        clientSecret: process.env.TWITCH_CLIENT_SECRET
      })
    ]
    ...

```
