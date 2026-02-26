---
title: "Strava"
description: "원본 URL: https://next-auth.js.org/v3/providers/strava"
---

원본 URL: https://next-auth.js.org/v3/providers/strava

# Strava | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/strava#documentation "Direct link to heading")

<http://developers.strava.com/docs/reference/>

## 옵션[​](https://next-auth.js.org/v3/providers/strava#options "Direct link to heading")

**Strava Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Strava Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/strava.js)

자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다. `redirect_uri` 설정이 요구 사항에 맞는지 확인하세요.

## 예시[​](https://next-auth.js.org/v3/providers/strava#example "Direct link to heading")

```
    import Providers from 'next-auth/providers'
    ...
    providers: [
      Providers.Strava({
        clientId: process.env.STRAVA_CLIENT_ID,
        clientSecret: process.env.STRAVA_CLIENT_SECRET,
      })
    ]
    ...

```
