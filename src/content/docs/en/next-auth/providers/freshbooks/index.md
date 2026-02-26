---
title: "Freshbooks"
description: "The Freshbooks Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/freshbooks

# Freshbooks | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/freshbooks#documentation "Direct link to heading")

<https://www.freshbooks.com/api/authenticating-with-oauth-2-0-on-the-new-freshbooks-api>

## Configuration[​](https://next-auth.js.org/providers/freshbooks#configuration "Direct link to heading")

<https://my.freshbooks.com/#/developer>

## Options[​](https://next-auth.js.org/providers/freshbooks#options "Direct link to heading")

The Freshbooks Provider comes with a set of default options:

<https://www.freshbooks.com/api/start>

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/freshbooks#example "Direct link to heading")

```
    import FreshbooksProvider from "next-auth/providers/freshbooks";
    ...
    providers: [
      FreshbooksProvider({
        clientId: process.env.FRESHBOOKS_CLIENT_ID,
        clientSecret: process.env.FRESHBOOKS_CLIENT_SECRET,
      })
    ]
    ...

```
