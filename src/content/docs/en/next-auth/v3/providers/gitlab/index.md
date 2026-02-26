---
title: "GitLab"
description: "The Gitlab Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/gitlab

# GitLab | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/gitlab#documentation "Direct link to heading")

<https://docs.gitlab.com/ee/api/oauth2.html>

## Configuration[​](https://next-auth.js.org/v3/providers/gitlab#configuration "Direct link to heading")

<https://gitlab.com/profile/applications>

## Options[​](https://next-auth.js.org/v3/providers/gitlab#options "Direct link to heading")

The **Gitlab Provider** comes with a set of default options:

- [Gitlab Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/gitlab.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/gitlab#example "Direct link to heading")

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

tip

Enable the _"read_user"_ option in scope if you want to save the users email address on sign up.
