---
title: "GitHub"
description: "GitHub는 에 숫자형 필드인 를 반환합니다. 자세한 내용은 docs를 참고하세요. Adapter를 사용하는 경우를 대비해, 이 필드를 데이터베이스 스키마에 추가하는 것을 잊지 마세요."
---

소스 URL: https://next-auth.js.org/providers/github

# GitHub | NextAuth.js

버전: v4

GitHub는 `Account`에 숫자형 필드인 `refresh_token_expires_in`를 반환합니다. 자세한 내용은 [docs](https://docs.github.com/en/developers/apps/building-github-apps/refreshing-user-to-server-access-tokens#response)를 참고하세요. [Adapter](https://authjs.dev/getting-started/database)를 사용하는 경우를 대비해, 이 필드를 데이터베이스 스키마에 추가하는 것을 잊지 마세요.

## 문서[​](https://next-auth.js.org/providers/github#documentation "Direct link to heading")

<https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps>

## 구성[​](https://next-auth.js.org/providers/github#configuration "Direct link to heading")

<https://github.com/settings/apps>

info

GitHub App을 생성할 때 GitHub의 비공개 이메일 주소에 접근하려면 "Email addresses" 계정 권한을 반드시 read-only로 설정하세요.

## 옵션[​](https://next-auth.js.org/providers/github#options "Direct link to heading")

**GitHub Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [GitHub Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/github.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/github#example "Direct link to heading")

```
    import GitHubProvider from "next-auth/providers/github";
    ...
    providers: [
      GitHubProvider({
        clientId: process.env.GITHUB_ID,
        clientSecret: process.env.GITHUB_SECRET
      })
    ]
    ...

```

danger

Client ID / Client Secret당 콜백 URL은 하나만 허용됩니다.

tip

사용자 프로필에 공개 이메일 주소가 없더라도 이메일 주소는 항상 반환됩니다.
