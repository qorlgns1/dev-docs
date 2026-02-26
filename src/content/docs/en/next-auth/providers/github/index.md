---
title: "GitHub"
description: "GitHub returns a field on  called  which is a number. See their docs. Remember to add this field to your database schema, in case if you are using an ..."
---

Source URL: https://next-auth.js.org/providers/github

# GitHub | NextAuth.js

Version: v4

GitHub returns a field on `Account` called `refresh_token_expires_in` which is a number. See their [docs](https://docs.github.com/en/developers/apps/building-github-apps/refreshing-user-to-server-access-tokens#response). Remember to add this field to your database schema, in case if you are using an [Adapter](https://authjs.dev/getting-started/database).

## Documentation[​](https://next-auth.js.org/providers/github#documentation "Direct link to heading")

<https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps>

## Configuration[​](https://next-auth.js.org/providers/github#configuration "Direct link to heading")

<https://github.com/settings/apps>

info

When creating a GitHub App, make sure to set the "Email addresses" account permission to read-only in order to access private email addresses on GitHub.

## Options[​](https://next-auth.js.org/providers/github#options "Direct link to heading")

The **GitHub Provider** comes with a set of default options:

- [GitHub Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/github.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/github#example "Direct link to heading")

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

Only allows one callback URL per Client ID / Client Secret.

tip

Email address is always returned, even if the user doesn't have a public email address on their profile.
