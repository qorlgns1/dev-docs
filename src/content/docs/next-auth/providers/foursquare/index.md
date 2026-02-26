---
title: "Foursquare"
description: 'Foursquare는 추가로  형식의  파라미터를 요구하며, 이는 본질적으로 "이 날짜까지의 API 변경 사항에 대비되어 있다"는 의미입니다.'
---

Source URL: https://next-auth.js.org/providers/foursquare

# Foursquare | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/foursquare#documentation "제목으로 직접 연결되는 링크")

<https://developer.foursquare.com/docs/places-api/authentication/#web-applications>

## 구성[​](https://next-auth.js.org/providers/foursquare#configuration "제목으로 직접 연결되는 링크")

<https://developer.foursquare.com/>

danger

Foursquare는 추가로 [`YYYYMMDD` 형식](https://developer.foursquare.com/docs/places-api/versioning/)의 `apiVersion` 파라미터를 요구하며, 이는 본질적으로 "이 날짜까지의 API 변경 사항에 대비되어 있다"는 의미입니다.

## 옵션[​](https://next-auth.js.org/providers/foursquare#options "제목으로 직접 연결되는 링크")

**Foursquare Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Foursquare Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/foursquare.js)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/foursquare#example "제목으로 직접 연결되는 링크")

```
    import FourSquareProvider from "next-auth/providers/foursquare";
    ...
    providers: [
      FourSquareProvider({
        clientId: process.env.FOURSQUARE_CLIENT_ID,
        clientSecret: process.env.FOURSQUARE_CLIENT_SECRET,
        apiVersion: "YYYYMMDD"
      })
    ]
    ...

```
