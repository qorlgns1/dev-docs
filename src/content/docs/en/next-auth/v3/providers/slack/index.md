---
title: "Slack"
description: "The Slack Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/slack

# Slack | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/slack#documentation "Direct link to heading")

<https://api.slack.com/authentication> <https://api.slack.com/docs/sign-in-with-slack>

## Configuration[​](https://next-auth.js.org/v3/providers/slack#configuration "Direct link to heading")

<https://api.slack.com/apps>

## Options[​](https://next-auth.js.org/v3/providers/slack#options "Direct link to heading")

The **Slack Provider** comes with a set of default options:

- [Slack Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/slack.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/slack#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Slack({
        clientId: process.env.SLACK_CLIENT_ID,
        clientSecret: process.env.SLACK_CLIENT_SECRET
      })
    ]
    ...

```
