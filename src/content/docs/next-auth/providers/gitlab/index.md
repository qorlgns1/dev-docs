---
title: "GitLab"
description: "GitLab은 에 이라는 필드를 반환하며, 이 값은 숫자입니다. 자세한 내용은 해당 문서를 참고하세요. Adapter를 사용 중이라면, 데이터베이스 스키마에 이 필드를 optional로 추가하는 것을 잊지 마세요."
---

Source URL: https://next-auth.js.org/providers/gitlab

# GitLab | NextAuth.js

버전: v4

참고

GitLab은 `Account`에 `created_at`이라는 필드를 반환하며, 이 값은 숫자입니다. 자세한 내용은 해당 [문서](https://docs.gitlab.com/ee/api/oauth2.html)를 참고하세요. [Adapter](https://next-auth.js.org/adapters)를 사용 중이라면, 데이터베이스 스키마에 이 필드를 optional로 추가하는 것을 잊지 마세요.

## 문서[​](https://next-auth.js.org/providers/gitlab#documentation "Direct link to heading")

<https://docs.gitlab.com/ee/api/oauth2.html>

## 구성[​](https://next-auth.js.org/providers/gitlab#configuration "Direct link to heading")

<https://gitlab.com/-/profile/applications>

## 옵션[​](https://next-auth.js.org/providers/gitlab#options "Direct link to heading")

**Gitlab Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Gitlab Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/gitlab.ts)

필요에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/gitlab#example "Direct link to heading")

```
    import GitlabProvider from "next-auth/providers/gitlab";
    ...
    providers: [
      GitlabProvider({
        clientId: process.env.GITLAB_CLIENT_ID,
        clientSecret: process.env.GITLAB_CLIENT_SECRET
      })
    ]
    ...

```

팁

가입 시 사용자 이메일 주소를 저장하려면 scope에서 _"read_user"_ 옵션을 활성화하세요.
