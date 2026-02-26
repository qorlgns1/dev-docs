---
title: "Zitadel"
description: "The Redirect URIs used when creating the credentials must include your full domain and end in the callback path. For example:"
---

Source URL: https://next-auth.js.org/providers/zitadel

# Zitadel | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/zitadel#documentation "Direct link to heading")

<https://zitadel.com/docs/apis/openidoauth/endpoints>

## Configuration[​](https://next-auth.js.org/providers/zitadel#configuration "Direct link to heading")

<https://zitadel.com/docs/guides/integrate/oauth-recommended-flows>

The Redirect URIs used when creating the credentials must include your full domain and end in the callback path. For example:

- For production: `https://{YOUR_DOMAIN}/api/auth/callback/zitadel`
- For development: `http://localhost:3000/api/auth/callback/zitadel`

Make sure to enable **dev mode** in ZITADEL console to allow redirects for local development.

## Options[​](https://next-auth.js.org/providers/zitadel#options "Direct link to heading")

The **ZITADEL Provider** comes with a set of default options:

- [ZITADEL Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/zitadel.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/zitadel#example "Direct link to heading")

```
    import ZitadelProvider from "next-auth/providers/zitadel";
    ...
    providers: [
      ZitadelProvider({
        issuer: process.env.ZITADEL_ISSUER,
        clientId: process.env.ZITADEL_CLIENT_ID,
        clientSecret: process.env.ZITADEL_CLIENT_SECRET,
      })
    ]
    ...

```

If you need access to ZITADEL APIs or need additional information, make sure to add the corresponding scopes.

To get the full list of supported claims take a look [here](https://zitadel.com/docs/apis/openidoauth/endpoints).

```
    const options = {
      ...
      providers: [
        ZitadelProvider({
          clientId: process.env.ZITADEL_CLIENT_ID,
          authorization: {
            params: {
                scope: `openid email profile urn:zitadel:iam:org:project:id:${process.env.ZITADEL_PROJECT_ID}:aud`
            }
          }
        })
      ],
      ...
    }

```

:::

tip

ZITADEL also returns a `email_verified` boolean property in the profile.

You can use this property to restrict access to people with verified accounts.

```
    const options = {
      ...
      callbacks: {
        async signIn({ account, profile }) {
          if (account.provider === "zitadel") {
            return profile.email_verified;
          }
          return true; // Do different verification for other providers that don't have `email_verified`
        },
      }
      ...
    }

```
