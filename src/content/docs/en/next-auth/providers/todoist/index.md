---
title: "Todoist"
description: "The Todoist Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/todoist

# Todoist | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/todoist#documentation "Direct link to heading")

<https://developer.todoist.com/guides/#oauth>

## Configuration[​](https://next-auth.js.org/providers/todoist#configuration "Direct link to heading")

<https://developer.todoist.com/appconsole.html>

## Options[​](https://next-auth.js.org/providers/todoist#options "Direct link to heading")

The **Todoist Provider** comes with a set of default options:

- [Todoist Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/todoist.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/todoist#example "Direct link to heading")

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
