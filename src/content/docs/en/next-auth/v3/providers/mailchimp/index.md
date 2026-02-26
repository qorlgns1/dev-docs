---
title: "Mailchimp"
description: "The Mailchimp Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/mailchimp

# Mailchimp | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/mailchimp#documentation "Direct link to heading")

<https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/>

## Configuration[​](https://next-auth.js.org/v3/providers/mailchimp#configuration "Direct link to heading")

<https://admin.mailchimp.com/account/oauth2/client/>

## Options[​](https://next-auth.js.org/v3/providers/mailchimp#options "Direct link to heading")

The **Mailchimp Provider** comes with a set of default options:

- [Mailchimp Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/mailchimp.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/mailchimp#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Mailchimp({
        clientId: process.env.MAILCHIMP_CLIENT_ID,
        clientSecret: process.env.MAILCHIMP_CLIENT_SECRET
      })
    ]
    ...

```
