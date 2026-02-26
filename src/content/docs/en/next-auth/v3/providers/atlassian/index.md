---
title: "Atlassian"
description: "The Atlassian Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/atlassian

# Atlassian | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/atlassian#documentation "Direct link to heading")

<https://developer.atlassian.com/cloud/jira/platform/oauth-2-authorization-code-grants-3lo-for-apps/#implementing-oauth-2-0--3lo->

## Options[​](https://next-auth.js.org/v3/providers/atlassian#options "Direct link to heading")

The **Atlassian Provider** comes with a set of default options:

- [Atlassian Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/atlassian.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/atlassian#example "Direct link to heading")

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

## Instructions[​](https://next-auth.js.org/v3/providers/atlassian#instructions "Direct link to heading")

### Configuration[​](https://next-auth.js.org/v3/providers/atlassian#configuration "Direct link to heading")

tip

An app can be created at <https://developer.atlassian.com/apps/>

Under "Apis and features" in the side menu, configure the following for "OAuth 2.0 (3LO)":

- Redirect URL
  - http://localhost:3000/api/auth/callback/atlassian

danger

To enable access to Jira Platform REST API you must enable User Identity API and add `read:me` to your provider scope option.
