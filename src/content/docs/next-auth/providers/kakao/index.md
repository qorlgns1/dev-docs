---
title: "Kakao"
description: "원본 URL: https://next-auth.js.org/providers/kakao"
---

원본 URL: https://next-auth.js.org/providers/kakao

# Kakao | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/kakao#documentation "Direct link to heading")

<https://developers.kakao.com/product/kakaoLogin>

## 구성[​](https://next-auth.js.org/providers/kakao#configuration "Direct link to heading")

<https://developers.kakao.com/docs/latest/en/kakaologin/common>

## 옵션[​](https://next-auth.js.org/providers/kakao#options "Direct link to heading")

**Kakao Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Kakao Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/kakao.ts)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/kakao#example "Direct link to heading")

```
    import KakaoProvider from "next-auth/providers/kakao";
    ...
    providers: [
      KakaoProvider({
        clientId: process.env.KAKAO_CLIENT_ID,
        clientSecret: process.env.KAKAO_CLIENT_SECRET
      })
    ]
    ...

```

## 안내[​](https://next-auth.js.org/providers/kakao#instructions "Direct link to heading")

### 구성[​](https://next-auth.js.org/providers/kakao#configuration-1 "Direct link to heading")

`https://developers.kakao.com/console/app`에서 provider와 Kakao 애플리케이션을 생성하세요. 앱 설정의 Kakao Login에서 웹 앱을 활성화하고, 동의 항목을 변경한 뒤 콜백 URL을 구성하세요.
