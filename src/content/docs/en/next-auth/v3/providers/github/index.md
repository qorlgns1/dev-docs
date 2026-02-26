---
title: "GitHub"
description: "The Github Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/github

# GitHub | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/github#documentation "Direct link to heading")

<https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps>

## Configuration[​](https://next-auth.js.org/v3/providers/github#configuration "Direct link to heading")

<https://github.com/settings/apps>

## Options[​](https://next-auth.js.org/v3/providers/github#options "Direct link to heading")

The **Github Provider** comes with a set of default options:

- [Github Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/github.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/github#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.GitHub({
        clientId: process.env.GITHUB_CLIENT_ID,
        clientSecret: process.env.GITHUB_CLIENT_SECRET
      })
    ]
    ...

```

danger

Only allows one callback URL per Client ID / Client Secret.

tip

Email address is not returned if privacy settings are enabled.
