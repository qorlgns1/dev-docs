---
title: "Zitadel"
description: "원본 URL: https://next-auth.js.org/providers/zitadel"
---

원본 URL: https://next-auth.js.org/providers/zitadel

# Zitadel | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/zitadel#documentation "Direct link to heading")

<https://zitadel.com/docs/apis/openidoauth/endpoints>

## 구성[​](https://next-auth.js.org/providers/zitadel#configuration "Direct link to heading")

<https://zitadel.com/docs/guides/integrate/oauth-recommended-flows>

자격 증명을 생성할 때 사용하는 Redirect URI에는 전체 도메인이 포함되어야 하며 callback 경로로 끝나야 합니다. 예를 들어:

- 프로덕션의 경우: `https://{YOUR_DOMAIN}/api/auth/callback/zitadel`
- 개발의 경우: `http://localhost:3000/api/auth/callback/zitadel`

로컬 개발에서 리디렉션을 허용하려면 ZITADEL 콘솔에서 **dev mode**를 활성화하세요.

## 옵션[​](https://next-auth.js.org/providers/zitadel#options "Direct link to heading")

**ZITADEL Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [ZITADEL Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/zitadel.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/zitadel#example "Direct link to heading")

```
    import ZitadelProvider from "next-auth/providers/zitadel";
    ...
    providers: [
      ZitadelProvider({
        issuer: process.env.ZITADEL_ISSUER,
        clientId: process.env.ZITADEL_CLIENT_ID,
        clientSecret: process.env.ZITADEL_CLIENT_SECRET,
      })
    ]
    ...

```

ZITADEL API에 접근해야 하거나 추가 정보가 필요하다면, 해당하는 scope를 추가해야 합니다.

지원되는 claims의 전체 목록은 [여기](https://zitadel.com/docs/apis/openidoauth/endpoints)에서 확인하세요.

```
    const options = {
      ...
      providers: [
        ZitadelProvider({
          clientId: process.env.ZITADEL_CLIENT_ID,
          authorization: {
            params: {
                scope: `openid email profile urn:zitadel:iam:org:project:id:${process.env.ZITADEL_PROJECT_ID}:aud`
            }
          }
        })
      ],
      ...
    }

```

:::

tip

ZITADEL은 profile에 `email_verified` boolean 속성도 반환합니다.

이 속성을 사용해 검증된 계정을 가진 사용자로 접근을 제한할 수 있습니다.

```
    const options = {
      ...
      callbacks: {
        async signIn({ account, profile }) {
          if (account.provider === "zitadel") {
            return profile.email_verified;
          }
          return true; // Do different verification for other providers that don't have `email_verified`
        },
      }
      ...
    }

```
