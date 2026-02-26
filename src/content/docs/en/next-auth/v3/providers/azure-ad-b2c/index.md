---
title: "Azure Active Directory B2C"
description: "The Azure Active Directory Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/azure-ad-b2c

# Azure Active Directory B2C | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/azure-ad-b2c#documentation "Direct link to heading")

<https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow>

## Configuration[​](https://next-auth.js.org/v3/providers/azure-ad-b2c#configuration "Direct link to heading")

<https://docs.microsoft.com/en-us/azure/active-directory-b2c/tutorial-create-tenant>

## Options[​](https://next-auth.js.org/v3/providers/azure-ad-b2c#options "Direct link to heading")

The **Azure Active Directory Provider** comes with a set of default options:

- [Azure Active Directory Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/azure-ad-b2c.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/azure-ad-b2c#example "Direct link to heading")

- In <https://portal.azure.com/> -> Azure Active Directory create a new App Registration.
- Make sure to remember / copy
  - Application (client) ID
  - Directory (tenant) ID
- When asked for a redirection URL, use http://localhost:3000/api/auth/callback/azure-ad-b2c
- Create a new secret and remember / copy its value immediately, it will disappear.

In `.env.local` create the following entries:

```
    AZURE_CLIENT_ID=<copy Application (client) ID here>
    AZURE_CLIENT_SECRET=<copy generated secret value here>
    AZURE_TENANT_ID=<copy the tenant id here>

```

In `pages/api/auth/[...nextauth].js` find or add the AZURE entries:

```
    import Providers from 'next-auth/providers';
    ...
    providers: [
      Providers.AzureADB2C({
        clientId: process.env.AZURE_CLIENT_ID,
        clientSecret: process.env.AZURE_CLIENT_SECRET,
        scope: 'offline_access User.Read',
        tenantId: process.env.AZURE_TENANT_ID,
      }),
    ]
    ...

```
