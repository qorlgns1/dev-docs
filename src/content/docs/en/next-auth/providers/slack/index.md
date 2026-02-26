---
title: "Slack"
description: "Slack requires that the redirect URL of your app uses , even for local development. An easy workaround for this is using a service like  that creates ..."
---

Source URL: https://next-auth.js.org/providers/slack

# Slack | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/slack#documentation "Direct link to heading")

<https://api.slack.com/authentication> <https://api.slack.com/docs/sign-in-with-slack>

## Configuration[​](https://next-auth.js.org/providers/slack#configuration "Direct link to heading")

<https://api.slack.com/apps>

danger

Slack requires that the redirect URL of your app uses `https`, even for local development. An easy workaround for this is using a service like [`ngrok`](https://ngrok.com) that creates a secure tunnel to your app, using `https`. Remember to set the url as `NEXTAUTH_URL` as well.

![](https://i.imgur.com/ydYKTLD.png)

## Options[​](https://next-auth.js.org/providers/slack#options "Direct link to heading")

The **Slack Provider** comes with a set of default options:

- [Slack Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/slack.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/slack#example "Direct link to heading")

```
    import SlackProvider from "next-auth/providers/slack";
    ...
    providers: [
      SlackProvider({
        clientId: process.env.SLACK_CLIENT_ID,
        clientSecret: process.env.SLACK_CLIENT_SECRET
      })
    ]
    ...

```
