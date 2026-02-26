---
title: "Atlassian"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

원문 URL: https://next-auth.js.org/v3/providers/atlassian

# Atlassian | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/atlassian#documentation "헤딩으로 바로 가기")

<https://developer.atlassian.com/cloud/jira/platform/oauth-2-authorization-code-grants-3lo-for-apps/#implementing-oauth-2-0--3lo->

## 옵션[​](https://next-auth.js.org/v3/providers/atlassian#options "헤딩으로 바로 가기")

**Atlassian Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Atlassian Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/atlassian.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/atlassian#example "헤딩으로 바로 가기")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Atlassian({
        clientId: process.env.ATLASSIAN_CLIENT_ID,
        clientSecret: process.env.ATLASSIAN_CLIENT_SECRET,
        scope: 'write:jira-work read:jira-work read:jira-user offline_access read:me'
      })
    ]
    ...

```

## 안내[​](https://next-auth.js.org/v3/providers/atlassian#instructions "헤딩으로 바로 가기")

### 구성[​](https://next-auth.js.org/v3/providers/atlassian#configuration "헤딩으로 바로 가기")

팁

앱은 <https://developer.atlassian.com/apps/> 에서 생성할 수 있습니다.

사이드 메뉴의 "Apis and features" 아래에서 "OAuth 2.0 (3LO)"에 대해 다음을 설정하세요.

- Redirect URL
  - http://localhost:3000/api/auth/callback/atlassian

주의

Jira Platform REST API에 대한 액세스를 활성화하려면 User Identity API를 활성화하고 provider scope 옵션에 `read:me`를 추가해야 합니다.
