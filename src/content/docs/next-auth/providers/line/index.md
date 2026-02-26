---
title: "LINE"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/line

# LINE | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/line#documentation "Direct link to heading")

<https://developers.line.biz/en/docs/line-login/integrate-line-login/>

## 구성[​](https://next-auth.js.org/providers/line#configuration "Direct link to heading")

<https://developers.line.biz/console/>

## 옵션[​](https://next-auth.js.org/providers/line#options "Direct link to heading")

**Line Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Line Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/line.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/line#example "Direct link to heading")

```
    import LineProvider from "next-auth/providers/line";
    ...
    providers: [
      LineProvider({
        clientId: process.env.LINE_CLIENT_ID,
        clientSecret: process.env.LINE_CLIENT_SECRET
      })
    ]
    ...

```

## 안내[​](https://next-auth.js.org/providers/line#instructions "Direct link to heading")

### 구성[​](https://next-auth.js.org/providers/line#configuration-1 "Direct link to heading")

`https://developers.line.biz/console/`에서 provider와 LINE 로그인 채널을 생성하세요. LINE Login 아래의 채널 설정에서 웹 앱을 활성화하고 다음을 구성하세요.

- Callback URL
  - http://localhost:3000/api/auth/callback/line

팁

이메일 주소를 가져오려면 Email address permission을 신청해야 합니다. [Line Developer Console](https://developers.line.biz/console/)을 열고 Login Channel로 이동하세요. 아래로 스크롤하여 **OpenID Connect** -> **Email address permission**을 찾으세요. **Apply**를 클릭하고 안내를 따르세요.
