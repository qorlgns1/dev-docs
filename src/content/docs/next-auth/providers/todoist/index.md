---
title: "Todoist"
description: "사용 사례에 맞게 옵션을 자유롭게 재정의할 수 있습니다."
---

원문 URL: https://next-auth.js.org/providers/todoist

# Todoist | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/todoist#documentation "Direct link to heading")

<https://developer.todoist.com/guides/#oauth>

## 설정[​](https://next-auth.js.org/providers/todoist#configuration "Direct link to heading")

<https://developer.todoist.com/appconsole.html>

## 옵션[​](https://next-auth.js.org/providers/todoist#options "Direct link to heading")

**Todoist Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Todoist Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/todoist.ts)

사용 사례에 맞게 옵션을 자유롭게 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/todoist#example "Direct link to heading")

```
    import TodoistProvider from "next-auth/providers/todoist";

    ...
    providers: [
      TodoistProvider({
        clientId: process.env.TODOIST_ID,
        clientSecret: process.env.TODOIST_SECRET
      })
    ]
    ...

```
