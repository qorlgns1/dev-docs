---
title: "Atlassian"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/atlassian

# Atlassian | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/atlassian#documentation "헤딩으로 직접 연결")

<https://developer.atlassian.com/cloud/jira/platform/oauth-2-authorization-code-grants-3lo-for-apps/#implementing-oauth-2-0--3lo->

## 옵션[​](https://next-auth.js.org/providers/atlassian#options "헤딩으로 직접 연결")

**Atlassian Provider**에는 다음과 같은 기본 옵션 세트가 포함되어 있습니다:

- [Atlassian Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/atlassian.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/atlassian#example "헤딩으로 직접 연결")

```
    import AtlassianProvider from "next-auth/providers/atlassian";
    ...
    providers: [
      AtlassianProvider({
        clientId: process.env.ATLASSIAN_CLIENT_ID,
        clientSecret: process.env.ATLASSIAN_CLIENT_SECRET,
        authorization: {
          params: {
            scope: "write:jira-work read:jira-work read:jira-user offline_access read:me"
          }
        }
      })
    ]
    ...

```

## 안내[​](https://next-auth.js.org/providers/atlassian#instructions "헤딩으로 직접 연결")

### 구성[​](https://next-auth.js.org/providers/atlassian#configuration "헤딩으로 직접 연결")

tip

앱은 <https://developer.atlassian.com/apps/> 에서 생성할 수 있습니다.

사이드 메뉴의 "Apis and features"에서 "OAuth 2.0 (3LO)"에 대해 다음을 구성하세요:

- Redirect URL
  - http://localhost:3000/api/auth/callback/atlassian

danger

Jira Platform REST API 접근을 활성화하려면 User Identity API를 활성화하고 provider scope 옵션에 `read:me`를 추가해야 합니다.
