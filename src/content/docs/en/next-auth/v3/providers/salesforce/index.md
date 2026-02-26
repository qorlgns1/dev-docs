---
title: "Salesforce"
description: "The Salesforce Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/salesforce

# Salesforce | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/salesforce#documentation "Direct link to heading")

[https://help.salesforce.com/articleView?id=remoteaccess_authenticate.htm&type=5](https://help.salesforce.com/articleView?id=remoteaccess_authenticate.htm&type=5)

## Options[​](https://next-auth.js.org/v3/providers/salesforce#options "Direct link to heading")

The **Salesforce Provider** comes with a set of default options:

- [Salesforce Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/salesforce.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/salesforce#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Salesforce({
        clientId: process.env.SALESFORCE_CLIENT_ID,
        clientSecret: process.env.SALESFORCE_CLIENT_SECRET,
      })
    ]
    ...

```
