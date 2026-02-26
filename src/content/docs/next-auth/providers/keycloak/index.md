---
title: "Keycloak"
description: 'Keycloak에서 "Access Type"을 "confidential"로 설정해 openid-connect 클라이언트를 생성하세요.'
---

출처 URL: https://next-auth.js.org/providers/keycloak

# Keycloak | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/keycloak#documentation "Direct link to heading")

<https://www.keycloak.org/docs/latest/server_admin/#_oidc_clients>

## 구성[​](https://next-auth.js.org/providers/keycloak#configuration "Direct link to heading")

팁

Keycloak에서 "Access Type"을 "confidential"로 설정해 openid-connect 클라이언트를 생성하세요.

## 옵션[​](https://next-auth.js.org/providers/keycloak#options "Direct link to heading")

**Keycloak Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Keycloak Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/keycloak.ts)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/keycloak#example "Direct link to heading")

```
    import KeycloakProvider from "next-auth/providers/keycloak";
    ...
    providers: [
      KeycloakProvider({
        clientId: process.env.KEYCLOAK_ID,
        clientSecret: process.env.KEYCLOAK_SECRET,
        issuer: process.env.KEYCLOAK_ISSUER,
      })
    ]
    ...

```

참고

`issuer`에는 realm이 포함되어야 합니다. 예: `https://my-keycloak-domain.com/realms/My_Realm`
