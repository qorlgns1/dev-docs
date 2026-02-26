---
title: "Basecamp"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/basecamp

# Basecamp | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/basecamp#documentation "Direct link to heading")

<https://github.com/basecamp/api/blob/master/sections/authentication.md>

## 구성[​](https://next-auth.js.org/v3/providers/basecamp#configuration "Direct link to heading")

<https://launchpad.37signals.com/integrations>

## 옵션[​](https://next-auth.js.org/v3/providers/basecamp#options "Direct link to heading")

**Basecamp Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Basecamp Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/basecamp.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/basecamp#examples "Direct link to heading")

### 기본 프로필 정보[​](https://next-auth.js.org/v3/providers/basecamp#basic-profile-information "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Basecamp({
        clientId: process.env.BASECAMP_CLIENT_ID,
        clientSecret: process.env.BASECAMP_CLIENT_SECRET
      })
    ]
    ...

```

note

위 예제를 사용하면 account id, email, name과 같은 프로필 정보만 가져올 수 있습니다. 특정 팀과 관련된 사용자 데이터를 가져오려면, 아래 예제처럼 다른 profileUrl과 프로필 정보를 처리하는 사용자 정의 함수를 제공해야 합니다.

### 특정 팀 관련 프로필 정보[​](https://next-auth.js.org/v3/providers/basecamp#profile-information-in-relation-to-specific-team "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Basecamp({
        clientId: process.env.BASECAMP_CLIENT_ID,
        clientSecret: process.env.BASECAMP_CLIENT_SECRET,
        profileUrl: `https://3.basecampapi.com/${process.env.BASECAMP_TEAM_ID}/my/profile.json`,
        profile: (profile) => {
          return {
            id: profile.id,
            name: profile.name,
            email: profile.email_address,
            image: profile.avatar_url,
            admin: profile.admin,
            owner: profile.owner
          }
        }
      })
    ]
    ...

```

tip

BASECAMP_TEAM_ID는 팀 홈페이지의 url 경로에서 찾을 수 있습니다. 예를 들어 url이 `https://3.basecamp.com/1234567/projects`라면, 이 경우 BASECAMP_TEAM_ID는 [`1234567`](https://github.com/nextauthjs/next-auth/commit/1234567)입니다.
