---
title: "EVE Online"
description: "자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

원문 URL: https://next-auth.js.org/providers/eveonline

# EVE Online | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/eveonline#documentation "Direct link to heading")

<https://developers.eveonline.com/blog/article/sso-to-authenticated-calls>

## 설정[​](https://next-auth.js.org/providers/eveonline#configuration "Direct link to heading")

<https://developers.eveonline.com/>

## 옵션[​](https://next-auth.js.org/providers/eveonline#options "Direct link to heading")

**EVE Online Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [EVE Online Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/eveonline.ts)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/eveonline#example "Direct link to heading")

```
    import EVEOnlineProvider from "next-auth/providers/eveonline";
    ...
    providers: [
      EVEOnlineProvider({
        clientId: process.env.EVE_CLIENT_ID,
        clientSecret: process.env.EVE_CLIENT_SECRET
      })
    ]
    ...

```

애플리케이션을 생성할 때 연결 유형으로 `Authentication Only`를 선택해야 합니다.

```
    ...
    options: {
      jwt: {
        secret: process.env.JWT_SECRET,
      },
      callbacks: {
        session: async ({ session, token }) => {
          session.user.id = token.id;
          return session;
        }
      }
    }
    ...

```
