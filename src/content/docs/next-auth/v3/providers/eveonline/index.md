---
title: "EVE Online"
description: "사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/eveonline

# EVE Online | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/eveonline#documentation "Direct link to heading")

<https://developers.eveonline.com/blog/article/sso-to-authenticated-calls>

## 구성[​](https://next-auth.js.org/v3/providers/eveonline#configuration "Direct link to heading")

<https://developers.eveonline.com/>

## 옵션[​](https://next-auth.js.org/v3/providers/eveonline#options "Direct link to heading")

**EVE Online Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [EVE Online Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/eveonline.js)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/eveonline#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.EVEOnline({
        clientId: process.env.EVE_CLIENT_ID,
        clientSecret: process.env.EVE_CLIENT_SECRET
      })
    ]
    ...

```

애플리케이션을 만들 때 연결 유형으로 `Authentication Only`를 선택해야 합니다.

```
    ...
    options: {
      jwt: {
        secret: process.env.JWT_SECRET,
      },
      callbacks: {
        jwt: async (token, user, account, profile, isNewUser) => {
          if (profile) {
            token = {
              ...token,
              id: profile.CharacterID,
            }
          }
          return token;
        },
        session: async (session, token) => {
          if (token) {
            session.user.id = token.id;
          }
          return session;
        }
      }
    }
    ...

```
