---
title: "Atlassian"
description: "The Atlassian Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/atlassian

# Atlassian | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/atlassian#documentation "Direct link to heading")

<https://developer.atlassian.com/cloud/jira/platform/oauth-2-authorization-code-grants-3lo-for-apps/#implementing-oauth-2-0--3lo->

## Options[​](https://next-auth.js.org/providers/atlassian#options "Direct link to heading")

The **Atlassian Provider** comes with a set of default options:

- [Atlassian Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/atlassian.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/atlassian#example "Direct link to heading")

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

## Instructions[​](https://next-auth.js.org/providers/atlassian#instructions "Direct link to heading")

### Configuration[​](https://next-auth.js.org/providers/atlassian#configuration "Direct link to heading")

tip

An app can be created at <https://developer.atlassian.com/apps/>

Under "Apis and features" in the side menu, configure the following for "OAuth 2.0 (3LO)":

- Redirect URL
  - http://localhost:3000/api/auth/callback/atlassian

danger

To enable access to Jira Platform REST API you must enable User Identity API and add `read:me` to your provider scope option.
