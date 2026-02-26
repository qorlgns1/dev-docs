---
title: "GitLab"
description: "원본 URL: https://next-auth.js.org/v3/providers/gitlab"
---

원본 URL: https://next-auth.js.org/v3/providers/gitlab

# GitLab | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/gitlab#documentation "제목으로 바로 가는 링크")

<https://docs.gitlab.com/ee/api/oauth2.html>

## 구성[​](https://next-auth.js.org/v3/providers/gitlab#configuration "제목으로 바로 가는 링크")

<https://gitlab.com/profile/applications>

## 옵션[​](https://next-auth.js.org/v3/providers/gitlab#options "제목으로 바로 가는 링크")

**Gitlab Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Gitlab Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/gitlab.js)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/gitlab#example "제목으로 바로 가는 링크")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.GitLab({
        clientId: process.env.GITLAB_CLIENT_ID,
        clientSecret: process.env.GITLAB_CLIENT_SECRET
      })
    ]
    ...

```

팁

가입 시 사용자의 이메일 주소를 저장하려면 scope에서 _"read_user"_ 옵션을 활성화하세요.
