---
title: "Salesforce"
description: "The Salesforce Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/salesforce

# Salesforce | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/salesforce#documentation "Direct link to heading")

[https://help.salesforce.com/articleView?id=remoteaccess_authenticate.htm&type=5](https://help.salesforce.com/articleView?id=remoteaccess_authenticate.htm&type=5)

## Options[​](https://next-auth.js.org/providers/salesforce#options "Direct link to heading")

The **Salesforce Provider** comes with a set of default options:

- [Salesforce Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/salesforce.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/salesforce#example "Direct link to heading")

```
    import SalesforceProvider from "next-auth/providers/salesforce";
    ...
    providers: [
      SalesforceProvider({
        clientId: process.env.SALESFORCE_CLIENT_ID,
        clientSecret: process.env.SALESFORCE_CLIENT_SECRET,
      })
    ]
    ...

```
