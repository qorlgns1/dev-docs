---
title: "Trakt"
description: "프로덕션에서 api.trakt.tv를 호출해 API를 사용한다면, 아래 예시를 따르세요. api-staging.trakt.tv를 호출해 Trakt의 샌드박스 환경에서 개발하려면 URL만 변경하여 기본 옵션을 사용하세요."
---

Source URL: https://next-auth.js.org/providers/trakt

# Trakt | NextAuth.js

Version: v4

## 문서[​](https://next-auth.js.org/providers/trakt#documentation "Direct link to heading")

<https://trakt.docs.apiary.io/#reference/authentication-oauth>

## 구성[​](https://next-auth.js.org/providers/trakt#configuration "Direct link to heading")

프로덕션에서 [api.trakt.tv](https://api.trakt.tv)를 호출해 API를 사용한다면, 아래 예시를 따르세요. [api-staging.trakt.tv](https://api-staging.trakt.tv)를 호출해 Trakt의 샌드박스 환경에서 개발하려면 URL만 변경하여 기본 옵션을 사용하세요.

먼저 Trakt에서 [production](https://trakt.tv/oauth/applications/new) 또는 [development](https://staging.trakt.tv/oauth/applications/new)용 OAuth 앱을 생성하세요. 그런 다음 `.env`에 Client ID와 Client Secret을 `TRAKT_ID`, `TRAKT_SECRET`으로 설정하세요.

## 옵션[​](https://next-auth.js.org/providers/trakt#options "Direct link to heading")

**Trakt Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Trakt Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/trakt.ts)

원하는 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/trakt#example "Direct link to heading")

```
    providers: [
      TraktProvider({
        clientId: process.env.TRAKT_ID,
        clientSecret: process.env.TRAKT_SECRET,
      }),
    ]

```

danger

Trakt는 이미지 핫링크를 허용하지 않습니다. 인증된 사용자의 프로필 사진도 마찬가지입니다.

danger

Trakt는 인증된 사용자의 이메일을 제공하지 않습니다.
