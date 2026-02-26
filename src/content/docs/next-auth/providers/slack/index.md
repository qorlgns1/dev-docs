---
title: "Slack"
description: "원본 URL: https://next-auth.js.org/providers/slack"
---

원본 URL: https://next-auth.js.org/providers/slack

# Slack | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/slack#documentation "Direct link to heading")

<https://api.slack.com/authentication> <https://api.slack.com/docs/sign-in-with-slack>

## 구성[​](https://next-auth.js.org/providers/slack#configuration "Direct link to heading")

<https://api.slack.com/apps>

danger

Slack은 로컬 개발 환경에서도 앱의 리디렉션 URL에 `https` 사용을 요구합니다. 이를 쉽게 우회하는 방법은 [`ngrok`](https://ngrok.com) 같은 서비스를 사용해 앱으로 `https` 보안 터널을 만드는 것입니다. 이때 URL을 `NEXTAUTH_URL`로도 설정하는 것을 잊지 마세요.

![](https://i.imgur.com/ydYKTLD.png)

## 옵션[​](https://next-auth.js.org/providers/slack#options "Direct link to heading")

**Slack Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Slack Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/slack.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/slack#example "Direct link to heading")

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
