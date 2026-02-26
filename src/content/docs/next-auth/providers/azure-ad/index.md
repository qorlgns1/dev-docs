---
title: "Azure Active Directory"
description: "원본 URL: https://next-auth.js.org/providers/azure-ad"
---

원본 URL: https://next-auth.js.org/providers/azure-ad

# Azure Active Directory | NextAuth.js

버전: v4

참고

Azure Active Directory는 `Account`에서 다음 필드를 반환합니다:

- `token_type` (string)
- `expires_in` (number)
- `ext_expires_in` (number)
- `access_token` (string).

[Adapter](https://authjs.dev/getting-started/database)를 사용하는 경우를 대비해, 데이터베이스 스키마에 이 필드들을 추가하는 것을 잊지 마세요.

## 문서[​](https://next-auth.js.org/providers/azure-ad#documentation "Direct link to heading")

<https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow>

## 구성[​](https://next-auth.js.org/providers/azure-ad#configuration "Direct link to heading")

<https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app>

## 예시[​](https://next-auth.js.org/providers/azure-ad#example "Direct link to heading")

### 특정 Active Directory 사용자에게만 접근을 허용하려면:[​](https://next-auth.js.org/providers/azure-ad#to-allow-specific-active-directory-users-access "Direct link to heading")

- <https://portal.azure.com/>에서 "Microsoft Entra ID"를 검색한 다음, 조직을 선택합니다.
- 다음으로, 왼쪽 메뉴에서 "Manage" 아코디언을 펼치고 "App Registration"으로 이동해 새 등록을 만듭니다.
- "Who can use this application or access this API?" 항목을 특히 주의해서 설정하세요.
  - 여기서 특정 유형의 사용자 계정으로 접근 범위를 제한할 수 있습니다.
  - 내 테넌트만, 모든 azure 테넌트, 또는 모든 azure 테넌트와 공용 Microsoft 계정(Skype, Xbox, Outlook.com 등)
- 리디렉션 URL을 요청받으면 플랫폼 유형으로 "Web"을 선택하고 `https://yourapplication.com/api/auth/callback/azure-ad`를 사용하거나, 개발 환경에서는 `http://localhost:3000/api/auth/callback/azure-ad`를 사용합니다.
- App Registration 생성 후 "Client Credential"에서 Client secret을 생성합니다.
- 이제 다음 값을 복사합니다:
  - Application (client) ID
  - Directory (tenant) ID
  - Client secret (value)

`.env.local`에 다음 항목을 생성합니다:

```
    AZURE_AD_CLIENT_ID=<copy Application (client) ID here>
    AZURE_AD_CLIENT_SECRET=<copy generated client secret value here>
    AZURE_AD_TENANT_ID=<copy the tenant id here>

```

이렇게 하면 테넌트는 기본적으로 `common` authorization endpoint를 사용합니다. [자세한 내용은 여기](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols#endpoints)를 참고하세요.

API에 접근할 때 `ResourceNotFound` 오류 코드가 보이면 올바른 tenant ID를 사용하고 있는지 확인하세요. 예를 들어 개인 계정에 접근하려는 경우에는 tenant ID를 제공하면 안 됩니다. :::

참고

Azure AD는 프로필 이미지를 이미지 URL이 아니라 ArrayBuffer로 반환하므로, 이 provider는 이를 base64로 인코딩된 이미지 문자열로 변환해 대신 반환합니다. 참고: <https://docs.microsoft.com/en-us/graph/api/profilephoto-get?view=graph-rest-1.0#examples>. 기본 이미지 크기는 세션이 JWT로 저장되는 경우 [공간 부족](https://next-auth.js.org/faq#:~:text=What%20are%20the%20disadvantages%20of%20JSON%20Web%20Tokens%3F)을 피하기 위해 48x48입니다.

`pages/api/auth/[...nextauth].js`에서 `AzureAD` 항목을 찾거나 추가하세요:

```
    import AzureADProvider from "next-auth/providers/azure-ad";

    ...
    providers: [
      AzureADProvider({
        clientId: process.env.AZURE_AD_CLIENT_ID,
        clientSecret: process.env.AZURE_AD_CLIENT_SECRET,
        tenantId: process.env.AZURE_AD_TENANT_ID,
      }),
    ]
    ...

```
