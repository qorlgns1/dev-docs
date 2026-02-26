---
title: "HubSpot"
description: "원본 URL: https://next-auth.js.org/providers/hubspot"
---

원본 URL: https://next-auth.js.org/providers/hubspot

# HubSpot | NextAuth.js

버전: v4

note

HubSpot은 토큰 보유자에 대한 제한된 양의 정보만 반환합니다([docs](https://legacydocs.hubspot.com/docs/methods/oauth2/get-access-token-information) 참고). 또 다른 문제는 [여기](https://community.hubspot.com/t5/APIs-Integrations/Profile-photo-is-not-retrieved-with-User-API/m-p/325521)에서 논의된 것처럼 이름과 프로필 사진을 API를 통해 가져올 수 없다는 점입니다.

## 문서[​](https://next-auth.js.org/providers/hubspot#documentation "Direct link to heading")

<https://developers.hubspot.com/docs/api/oauth-quickstart-guide>

## 설정[​](https://next-auth.js.org/providers/hubspot#configuration "Direct link to heading")

<https://developers.hubspot.com/docs/api/developer-tools-overview>에 설명된 대로 Developer Account에 APP이 있어야 합니다.

## 옵션[​](https://next-auth.js.org/providers/hubspot#options "Direct link to heading")

**HubSpot Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [HubSpot Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/hubspot.ts)

자체 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/hubspot#example "Direct link to heading")

```
    import HubspotProvider from "next-auth/providers/hubspot";
    ...
    providers: [
      HubspotProvider({
        clientId: process.env.HUBSPOT_CLIENT_ID,
        clientSecret: process.env.HUBSPOT_CLIENT_SECRET
      })
    ]
    ...

```

danger

HubSpot App Settings 페이지의 **Auth** 탭 아래에 있는 **Redirect URL**은 콜백 URL과 일치해야 하며, 로컬 개발에서는 `http://localhost:3000/api/auth/callback/hubspot`가 됩니다. Client ID와 Client Secret 쌍당 하나의 콜백 URL만 허용되므로, URL 변경을 계속 조정하는 것보다 로컬 개발용 새 앱을 만드는 것이 더 쉬울 수 있습니다.
