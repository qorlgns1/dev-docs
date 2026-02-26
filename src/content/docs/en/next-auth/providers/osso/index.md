---
title: "Osso"
description: "Osso is an open source service that handles SAML authentication against Identity Providers, normalizes profiles, and makes those profiles available to..."
---

Source URL: https://next-auth.js.org/providers/osso

# Osso | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/osso#documentation "Direct link to heading")

Osso is an open source service that handles SAML authentication against Identity Providers, normalizes profiles, and makes those profiles available to you in an OAuth 2.0 code grant flow.

If you don't yet have an Osso instance, you can use [Osso's Demo App](https://demo.ossoapp.com) for your testing purposes. For documentation on deploying an Osso instance, see <https://ossoapp.com/docs/deploy/overview/>

## Configuration[​](https://next-auth.js.org/providers/osso#configuration "Direct link to heading")

You can configure your OAuth Clients on your Osso Admin UI, i.e. <https://demo.ossoapp.com/admin/config> \- you'll need to get a Client ID and Secret and allow-list your redirect URIs.

[SAML SSO differs a bit from OAuth](https://ossoapp.com/blog/saml-vs-oauth) \- for every tenant who wants to sign in to your application using SAML, you and your customer need to perform a multi-step configuration in Osso's Admin UI and the admin dashboard of the tenant's Identity Provider. Osso provides documentation for providers like Okta and OneLogin, cloud-based IDPs who also offer a developer account that's useful for testing. Osso also provides a [Mock IDP](https://idp.ossoapp.com) that you can use for testing without needing to sign up for an Identity Provider service.

See Osso's complete configuration and testing documentation at <https://ossoapp.com/docs/configure/overview>

## Options[​](https://next-auth.js.org/providers/osso#options "Direct link to heading")

The **Osso Provider** comes with a set of default options:

- [Osso Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/osso.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/osso#example "Direct link to heading")

A full example application is available at <https://github.com/enterprise-oss/osso-next-auth-example> and <https://nextjs-demo.ossoapp.com>

```
    import OssoProvider from "next-auth/providers/osso";
    ...
    providers: [
      OssoProvider({
        clientId: process.env.OSSO_CLIENT_ID,
        clientSecret: process.env.OSSO_CLIENT_SECRET,
        issuer: process.env.OSSO_ISSUER
      })
    }
    ...

```

note

`issuer` should be the fully qualified domain – e.g. `demo.ossoapp.com`
