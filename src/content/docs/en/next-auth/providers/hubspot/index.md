---
title: "HubSpot"
description: "HubSpot returns a limited amount of information on the token holder (see docs). One other issue is that the name and profile photo cannot be fetched t..."
---

Source URL: https://next-auth.js.org/providers/hubspot

# HubSpot | NextAuth.js

Version: v4

note

HubSpot returns a limited amount of information on the token holder (see [docs](https://legacydocs.hubspot.com/docs/methods/oauth2/get-access-token-information)). One other issue is that the name and profile photo cannot be fetched through API as discussed [here](https://community.hubspot.com/t5/APIs-Integrations/Profile-photo-is-not-retrieved-with-User-API/m-p/325521).

## Documentation[​](https://next-auth.js.org/providers/hubspot#documentation "Direct link to heading")

<https://developers.hubspot.com/docs/api/oauth-quickstart-guide>

## Configuration[​](https://next-auth.js.org/providers/hubspot#configuration "Direct link to heading")

You need to have an APP in your Developer Account as described at <https://developers.hubspot.com/docs/api/developer-tools-overview>

## Options[​](https://next-auth.js.org/providers/hubspot#options "Direct link to heading")

The **HubSpot Provider** comes with a set of default options:

- [HubSpot Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/hubspot.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/hubspot#example "Direct link to heading")

```
    import HubspotProvider from "next-auth/providers/hubspot";
    ...
    providers: [
      HubspotProvider({
        clientId: process.env.HUBSPOT_CLIENT_ID,
        clientSecret: process.env.HUBSPOT_CLIENT_SECRET
      })
    ]
    ...

```

danger

The **Redirect URL** under the **Auth** tab on the HubSpot App Settings page must match the callback url which would be http://localhost:3000/api/auth/callback/hubspot for local development. Only one callback URL per Client ID and Client Secret pair is allowed, so it might be easier to create a new app for local development then fiddle with the url changes.
