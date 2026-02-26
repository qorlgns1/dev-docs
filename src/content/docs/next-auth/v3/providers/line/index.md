---
title: "LINE"
description: "자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/v3/providers/line

# LINE | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/line#documentation "Direct link to heading")

<https://developers.line.biz/en/docs/line-login/integrate-line-login/>

## 설정[​](https://next-auth.js.org/v3/providers/line#configuration "Direct link to heading")

<https://developers.line.biz/console/>

## 옵션[​](https://next-auth.js.org/v3/providers/line#options "Direct link to heading")

**Line Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Line Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/line.js)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/line#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.LINE({
        clientId: process.env.LINE_CLIENT_ID,
        clientSecret: process.env.LINE_CLIENT_SECRET
      })
    ]
    ...

```

## 지침[​](https://next-auth.js.org/v3/providers/line#instructions "Direct link to heading")

### 설정[​](https://next-auth.js.org/v3/providers/line#configuration-1 "Direct link to heading")

`https://developers.line.biz/console/`에서 provider와 LINE 로그인 채널을 생성하세요. LINE Login 아래 채널 설정에서 웹 앱을 활성화하고 다음을 구성하세요:

- 콜백 URL
  - http://localhost:3000/api/auth/callback/line
