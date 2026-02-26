---
title: "42 School"
description: "42 returns a field on  called  which is a number. See the docs. Make sure to add this field to your database schema, in case if you are using an Adapt..."
---

Source URL: https://next-auth.js.org/providers/42-school

# 42 School | NextAuth.js

Version: v4

note

42 returns a field on `Account` called `created_at` which is a number. See the [docs](https://api.intra.42.fr/apidoc/guides/getting_started#make-basic-requests). Make sure to add this field to your database schema, in case if you are using an [Adapter](https://next-auth.js.org/adapters).

## Documentation[​](https://next-auth.js.org/providers/42-school#documentation "Direct link to heading")

<https://api.intra.42.fr/apidoc/guides/web_application_flow>

## Configuration[​](https://next-auth.js.org/providers/42-school#configuration "Direct link to heading")

<https://profile.intra.42.fr/oauth/applications/new>

## Options[​](https://next-auth.js.org/providers/42-school#options "Direct link to heading")

The **42 School Provider** comes with a set of default options:

- [42 School Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/42-school.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/42-school#example "Direct link to heading")

```
    import FortyTwoProvider from "next-auth/providers/42-school";
    ...
    providers: [
      FortyTwoProvider({
        clientId: process.env.FORTY_TWO_CLIENT_ID,
        clientSecret: process.env.FORTY_TWO_CLIENT_SECRET
      })
    ]
    ...

```
