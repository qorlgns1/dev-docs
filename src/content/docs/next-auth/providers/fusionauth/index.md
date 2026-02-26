---
title: "FusionAuth"
description: "원본 URL: https://next-auth.js.org/providers/fusionauth"
---

원본 URL: https://next-auth.js.org/providers/fusionauth

# FusionAuth | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/fusionauth#documentation "Direct link to heading")

<https://fusionauth.io/docs/v1/tech/oauth/>

## 옵션[​](https://next-auth.js.org/providers/fusionauth#options "Direct link to heading")

**FusionAuth Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [FusionAuth Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/fusionauth.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/fusionauth#example "Direct link to heading")

```
    import FusionAuthProvider from "next-auth/providers/fusionauth";
    ...
    providers: [
      FusionAuthProvider({
        id: "fusionauth",
        name: "FusionAuth",
        issuer:  process.env.FUSIONAUTH_ISSUER,
        clientId: process.env.FUSIONAUTH_CLIENT_ID,
        clientSecret: process.env.FUSIONAUTH_SECRET,
        tenantId: process.env.FUSIONAUTH_TENANT_ID // Only required if you're using multi-tenancy
      }),
    ]
    ...

```

danger

멀티 테넌시를 사용 중이라면, 올바른 테마를 적용하기 위해 `tenantId` 옵션을 전달해야 합니다.

## 안내[​](https://next-auth.js.org/providers/fusionauth#instructions "Direct link to heading")

### 구성[​](https://next-auth.js.org/providers/fusionauth#configuration "Direct link to heading")

tip

애플리케이션은 https://your-fusionauth-server-url/admin/application 에서 생성할 수 있습니다.

자세한 내용은 [FusionAuth 5-minute setup guide](https://fusionauth.io/docs/v1/tech/5-minute-setup-guide)를 참고하세요.

애플리케이션의 OAuth 설정에서 다음을 구성하세요.

- Redirect URL
  - http://localhost:3000/api/auth/callback/fusionauth
- Enabled grants
  - _Authorization Code_ 가 활성화되어 있는지 확인하세요.

JSON Web Tokens를 사용하는 경우, 서명 알고리즘이 RS256인지 확인해야 합니다. RS256 키 쌍은 Settings, Key Master로 이동한 뒤 RSA를 생성하고 알고리즘으로 SHA-256을 선택해 만들 수 있습니다. 그다음 애플리케이션의 JWT 설정으로 이동해 이 키를 Access Token signing key와 Id Token signing key로 선택하세요.
