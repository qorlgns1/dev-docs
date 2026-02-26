---
title: "Mailchimp"
description: "The Mailchimp Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/mailchimp

# Mailchimp | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/mailchimp#documentation "Direct link to heading")

<https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/>

## Configuration[​](https://next-auth.js.org/providers/mailchimp#configuration "Direct link to heading")

<https://admin.mailchimp.com/account/oauth2/client/>

## Options[​](https://next-auth.js.org/providers/mailchimp#options "Direct link to heading")

The **Mailchimp Provider** comes with a set of default options:

- [Mailchimp Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/mailchimp.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/mailchimp#example "Direct link to heading")

```
    import MailchimpProvider from "next-auth/providers/mailchimp";
    ...
    providers: [
      MailchimpProvider({
        clientId: process.env.MAILCHIMP_CLIENT_ID,
        clientSecret: process.env.MAILCHIMP_CLIENT_SECRET
      })
    ]
    ...

```
