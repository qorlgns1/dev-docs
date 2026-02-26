---
title: "Azure Active Directory B2C"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/v3/providers/azure-ad-b2c

# Azure Active Directory B2C | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/azure-ad-b2c#documentation "제목으로 바로 가는 링크")

<https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow>

## 구성[​](https://next-auth.js.org/v3/providers/azure-ad-b2c#configuration "제목으로 바로 가는 링크")

<https://docs.microsoft.com/en-us/azure/active-directory-b2c/tutorial-create-tenant>

## 옵션[​](https://next-auth.js.org/v3/providers/azure-ad-b2c#options "제목으로 바로 가는 링크")

**Azure Active Directory Provider**에는 기본 옵션 세트가 제공됩니다:

- [Azure Active Directory Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/azure-ad-b2c.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/azure-ad-b2c#example "제목으로 바로 가는 링크")

- <https://portal.azure.com/> -> Azure Active Directory에서 새 App Registration을 생성합니다.
- 다음 값을 반드시 기억하거나 복사해 두세요
  - Application (client) ID
  - Directory (tenant) ID
- 리디렉션 URL을 묻는 경우 http://localhost:3000/api/auth/callback/azure-ad-b2c 를 사용하세요.
- 새 secret을 생성하고 값을 즉시 기억하거나 복사해 두세요. 곧 사라집니다.

`.env.local`에 다음 항목을 생성하세요:

```
    AZURE_CLIENT_ID=<copy Application (client) ID here>
    AZURE_CLIENT_SECRET=<copy generated secret value here>
    AZURE_TENANT_ID=<copy the tenant id here>

```

`pages/api/auth/[...nextauth].js`에서 AZURE 항목을 찾거나 추가하세요:

```
    import Providers from 'next-auth/providers';
    ...
    providers: [
      Providers.AzureADB2C({
        clientId: process.env.AZURE_CLIENT_ID,
        clientSecret: process.env.AZURE_CLIENT_SECRET,
        scope: 'offline_access User.Read',
        tenantId: process.env.AZURE_TENANT_ID,
      }),
    ]
    ...

```
