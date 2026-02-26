---
title: "Slack"
description: "사용 사례에 맞게 옵션을 자유롭게 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/slack

# Slack | NextAuth.js

Version: v3

## 문서[​](https://next-auth.js.org/v3/providers/slack#documentation "Direct link to heading")

<https://api.slack.com/authentication> <https://api.slack.com/docs/sign-in-with-slack>

## 구성[​](https://next-auth.js.org/v3/providers/slack#configuration "Direct link to heading")

<https://api.slack.com/apps>

## 옵션[​](https://next-auth.js.org/v3/providers/slack#options "Direct link to heading")

**Slack Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Slack Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/slack.js)

사용 사례에 맞게 옵션을 자유롭게 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/slack#example "Direct link to heading")

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
