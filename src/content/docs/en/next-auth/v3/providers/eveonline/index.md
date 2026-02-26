---
title: "EVE Online"
description: "The EVE Online Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/eveonline

# EVE Online | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/eveonline#documentation "Direct link to heading")

<https://developers.eveonline.com/blog/article/sso-to-authenticated-calls>

## Configuration[​](https://next-auth.js.org/v3/providers/eveonline#configuration "Direct link to heading")

<https://developers.eveonline.com/>

## Options[​](https://next-auth.js.org/v3/providers/eveonline#options "Direct link to heading")

The **EVE Online Provider** comes with a set of default options:

- [EVE Online Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/eveonline.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/eveonline#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.EVEOnline({
        clientId: process.env.EVE_CLIENT_ID,
        clientSecret: process.env.EVE_CLIENT_SECRET
      })
    ]
    ...

```

When creating your application, make sure to select `Authentication Only` as the connection type.

```
    ...
    options: {
      jwt: {
        secret: process.env.JWT_SECRET,
      },
      callbacks: {
        jwt: async (token, user, account, profile, isNewUser) => {
          if (profile) {
            token = {
              ...token,
              id: profile.CharacterID,
            }
          }
          return token;
        },
        session: async (session, token) => {
          if (token) {
            session.user.id = token.id;
          }
          return session;
        }
      }
    }
    ...

```
