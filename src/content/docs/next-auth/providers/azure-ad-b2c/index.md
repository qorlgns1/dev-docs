---
title: "Azure Active Directory B2C"
description: "Azure AD B2C는 에서 다음 필드를 반환합니다:"
---

Source URL: https://next-auth.js.org/providers/azure-ad-b2c

# Azure Active Directory B2C | NextAuth.js

버전: v4

참고

Azure AD B2C는 `Account`에서 다음 필드를 반환합니다:

- `refresh_token_expires_in` (number)
- `not_before` (number)
- `id_token_expires_in` (number)
- `profile_info` (string).

자세한 내용은 [docs](https://docs.microsoft.com/en-us/azure/active-directory-b2c/access-tokens)를 참고하세요. [Adapter](https://next-auth.js.org/adapters)를 사용하는 경우를 대비해, 데이터베이스 스키마에 이 필드들을 추가하는 것을 잊지 마세요.

## 문서[​](https://next-auth.js.org/providers/azure-ad-b2c#documentation "Direct link to heading")

<https://docs.microsoft.com/azure/active-directory/develop/v2-oauth2-auth-code-flow>

## 구성[​](https://next-auth.js.org/providers/azure-ad-b2c#configuration "Direct link to heading")

<https://docs.microsoft.com/azure/active-directory-b2c/tutorial-create-tenant>

## 옵션[​](https://next-auth.js.org/providers/azure-ad-b2c#options "Direct link to heading")

**Azure Active Directory Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Azure Active Directory Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/azure-ad-b2c.ts)

각 옵션은 사용 사례에 맞게 재정의할 수 있습니다.

## 구성 (기본)[​](https://next-auth.js.org/providers/azure-ad-b2c#configuration-basic "Direct link to heading")

기본 구성은 Azure AD B2C가 ID Token을 반환하도록 설정합니다. 고급 구성을 진행하기 전에 사전 조건으로 먼저 수행해야 합니다.

1단계: Azure AD B2C Tenant <https://docs.microsoft.com/en-us/azure/active-directory-b2c/tutorial-create-tenant>

2단계: App Registration <https://docs.microsoft.com/en-us/azure/active-directory-b2c/tutorial-register-applications>

3단계: User Flow <https://docs.microsoft.com/en-us/azure/active-directory-b2c/tutorial-create-user-flows>

참고: "User attributes and token claims" 단계에서는 최소한 다음을 설정할 수 있습니다:

- Collect attribute:
  - Email Address
  - Display Name
  - Given Name
  - Surname
- Return claim:
  - Email Addresses
  - Display Name
  - Given Name
  - Surname
  - Identity Provider
  - Identity Provider Access Token
  - User's Object ID

## 예제[​](https://next-auth.js.org/providers/azure-ad-b2c#example "Direct link to heading")

`.env.local`에 다음 항목을 생성하세요:

```
    AZURE_AD_B2C_TENANT_NAME=<copy the B2C tenant name here from Step 1>
    AZURE_AD_B2C_CLIENT_ID=<copy Application (client) ID here from Step 2>
    AZURE_AD_B2C_CLIENT_SECRET=<copy generated secret value here from Step 2>
    AZURE_AD_B2C_PRIMARY_USER_FLOW=<copy the name of the signin user flow you created from Step 3>

```

`pages/api/auth/[...nextauth].js`에서 AZURE_AD_B2C 항목을 찾거나 추가하세요:

```
    import AzureADB2CProvider from "next-auth/providers/azure-ad-b2c";
    ...
    providers: [
      AzureADB2CProvider({
        tenantId: process.env.AZURE_AD_B2C_TENANT_NAME,
        clientId: process.env.AZURE_AD_B2C_CLIENT_ID,
        clientSecret: process.env.AZURE_AD_B2C_CLIENT_SECRET,
        primaryUserFlow: process.env.AZURE_AD_B2C_PRIMARY_USER_FLOW,
        authorization: { params: { scope: "offline_access openid" } },
      }),
    ]
    ...

```

## 구성 (고급)[​](https://next-auth.js.org/providers/azure-ad-b2c#configuration-advanced "Direct link to heading")

고급 구성은 Azure AD B2C가 Authorization Token을 반환하도록 설정합니다. 이는 위 기본 구성에서 완료한 단계를 기반으로 합니다.

4단계: Web API 애플리케이션 추가 <https://docs.microsoft.com/en-us/azure/active-directory-b2c/tutorial-single-page-app-webapi?tabs=app-reg-ga>

참고: 이는 두 번째 앱 등록(2단계와 유사)이며, 설정 및 구성이 다릅니다.

## 예제[​](https://next-auth.js.org/providers/azure-ad-b2c#example-1 "Direct link to heading")

여기서는 `.env.local`에서 변경할 내용이 없습니다. 유일한 업데이트는 `pages/api/auth/[...nextauth].js`에서, 위 4단계에서 생성한 추가 스코프를 넣어야 한다는 점입니다:

```
    import AzureADB2CProvider from "next-auth/providers/azure-ad-b2c";
    ...
    providers: [
      AzureADB2CProvider({
        tenantId: process.env.AZURE_AD_B2C_TENANT_NAME,
        clientId: process.env.AZURE_AD_B2C_CLIENT_ID,
        clientSecret: process.env.AZURE_AD_B2C_CLIENT_SECRET,
        primaryUserFlow: process.env.AZURE_AD_B2C_PRIMARY_USER_FLOW,
        authorization: { params: { scope: `https://${process.env.AZURE_AD_B2C_TENANT_NAME}.onmicrosoft.com/api/demo.read https://${process.env.AZURE_AD_B2C_TENANT_NAME}.onmicrosoft.com/api/demo.write offline_access openid` } },
      }),
    ]
    ...

```
