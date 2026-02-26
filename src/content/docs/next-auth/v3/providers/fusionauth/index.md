---
title: "FusionAuth"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/v3/providers/fusionauth

# FusionAuth | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/fusionauth#documentation "제목으로 직접 연결")

<https://fusionauth.io/docs/v1/tech/oauth/>

## 옵션[​](https://next-auth.js.org/v3/providers/fusionauth#options "제목으로 직접 연결")

**FusionAuth Provider**에는 다음과 같은 기본 옵션 세트가 포함되어 있습니다:

- [FusionAuth Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/fusionauth.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/fusionauth#example "제목으로 직접 연결")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.FusionAuth({
        id: "fusionauth",
        name: "FusionAuth",
        domain:  process.env.FUSIONAUTH_DOMAIN,
        clientId: process.env.FUSIONAUTH_CLIENT_ID,
        clientSecret: process.env.FUSIONAUTH_SECRET,
        tenantId: process.env.FUSIONAUTH_TENANT_ID // Only required if you're using multi-tenancy
      }),
    ]
    ...

```

danger

멀티 테넌시를 사용하는 경우, 올바른 테마를 적용하려면 `tenantId` 옵션을 전달해야 합니다.

## 안내[​](https://next-auth.js.org/v3/providers/fusionauth#instructions "제목으로 직접 연결")

### 구성[​](https://next-auth.js.org/v3/providers/fusionauth#configuration "제목으로 직접 연결")

tip

애플리케이션은 https://your-fusionauth-server-url/admin/application 에서 생성할 수 있습니다.

자세한 내용은 [FusionAuth 5-minute setup guide](https://fusionauth.io/docs/v1/tech/5-minute-setup-guide)를 참고하세요.

애플리케이션의 OAuth 설정에서 다음을 구성하세요.

- Redirect URL
  - https://localhost:3000/api/auth/callback/fusionauth
- Enabled grants
  - _Authorization Code_ 가 활성화되어 있는지 확인하세요.
