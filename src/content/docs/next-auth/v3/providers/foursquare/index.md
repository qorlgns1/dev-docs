---
title: "Foursquare"
description: 'Foursquare는 추가  파라미터를  format으로 요구하며, 이는 본질적으로 "이 날짜까지의 API 변경 사항을 감당할 준비가 되어 있다"는 의미입니다.'
---

소스 URL: https://next-auth.js.org/v3/providers/foursquare

# Foursquare | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/foursquare#documentation "헤딩으로 바로 가는 링크")

<https://developer.foursquare.com/docs/places-api/authentication/#web-applications>

## 구성[​](https://next-auth.js.org/v3/providers/foursquare#configuration "헤딩으로 바로 가는 링크")

<https://developer.foursquare.com/>

danger

Foursquare는 추가 `apiVersion` 파라미터를 [`YYYYMMDD` format](https://developer.foursquare.com/docs/places-api/versioning/)으로 요구하며, 이는 본질적으로 "이 날짜까지의 API 변경 사항을 감당할 준비가 되어 있다"는 의미입니다.

## 옵션[​](https://next-auth.js.org/v3/providers/foursquare#options "헤딩으로 바로 가는 링크")

**Foursquare Provider**는 다음과 같은 기본 옵션 세트를 제공합니다:

- [Foursquare Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/foursquare.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/foursquare#example "헤딩으로 바로 가는 링크")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Foursquare({
        clientId: process.env.FOURSQUARE_CLIENT_ID,
        clientSecret: process.env.FOURSQUARE_CLIENT_SECRET,
        apiVersion: 'YYYYMMDD'
      })
    ]
    ...

```
