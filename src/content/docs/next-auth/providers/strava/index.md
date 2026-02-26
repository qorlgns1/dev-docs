---
title: "Strava"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.  구성이 필요에 맞는지 확인하세요."
---

Source URL: https://next-auth.js.org/providers/strava

# Strava | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/strava#documentation "Direct link to heading")

<http://developers.strava.com/docs/reference/>

## 옵션[​](https://next-auth.js.org/providers/strava#options "Direct link to heading")

**Strava Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Strava Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/strava.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다. `redirect_uri` 구성이 필요에 맞는지 확인하세요.

## 예시[​](https://next-auth.js.org/providers/strava#example "Direct link to heading")

```
    import StravaProvider from "next-auth/providers/strava";
    ...
    providers: [
      StravaProvider({
        clientId: process.env.STRAVA_CLIENT_ID,
        clientSecret: process.env.STRAVA_CLIENT_SECRET,
      })
    ]
    ...

```
