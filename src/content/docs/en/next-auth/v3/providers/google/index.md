---
title: "Google"
description: "The Google Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/google

# Google | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/google#documentation "Direct link to heading")

<https://developers.google.com/identity/protocols/oauth2>

## Configuration[​](https://next-auth.js.org/v3/providers/google#configuration "Direct link to heading")

<https://console.developers.google.com/apis/credentials>

## Options[​](https://next-auth.js.org/v3/providers/google#options "Direct link to heading")

The **Google Provider** comes with a set of default options:

- [Google Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/google.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/google#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Google({
        clientId: process.env.GOOGLE_CLIENT_ID,
        clientSecret: process.env.GOOGLE_CLIENT_SECRET
      })
    ]
    ...

```

danger

Google only provide the Refresh Token to an application the first time a user signs in.

To force Google to re-issue a Refresh Token, the user needs to remove the application from their account and sign in again: <https://myaccount.google.com/permissions>

Alternatively, you can also pass options in the `authorizationUrl` which will force the Refresh Token to always be provided on sign in, however this will ask all users to confirm if they wish to grant your application access every time they sign in.

If you need access to the RefreshToken or AccessToken for a Google account and you are not using a database to persist user accounts, this may be something you need to do.

```
    const options = {
      ...
      providers: [
        Providers.Google({
          clientId: process.env.GOOGLE_ID,
          clientSecret: process.env.GOOGLE_SECRET,
          authorizationUrl: 'https://accounts.google.com/o/oauth2/v2/auth?prompt=consent&access_type=offline&response_type=code',
        })
      ],
      ...
    }

```

tip

Google also return an `verified_email` boolean property in the OAuth profile.

You can use this property to restrict access to people with verified accounts at a particular domain.

```
    const options = {
      ...
      callbacks: {
        async signIn(user, account, profile) {
          if (account.provider === 'google' &&
              profile.verified_email === true &&
              profile.email.endsWith('@example.com')) {
            return true
          } else {
            return false
          }
        },
      }
      ...
    }

```
