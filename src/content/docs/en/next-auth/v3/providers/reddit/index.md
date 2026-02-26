---
title: "Reddit"
description: "The Reddit Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/reddit

# Reddit | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/reddit#documentation "Direct link to heading")

<https://www.reddit.com/dev/api/>

## Configuration[​](https://next-auth.js.org/v3/providers/reddit#configuration "Direct link to heading")

<https://www.reddit.com/prefs/apps/>

## Options[​](https://next-auth.js.org/v3/providers/reddit#options "Direct link to heading")

The **Reddit Provider** comes with a set of default options:

- [Reddit Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/reddit.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/reddit#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Reddit({
        clientId: process.env.REDDIT_CLIENT_ID,
        clientSecret: process.env.REDDIT_CLIENT_SECRET
      })
    ]
    ...

```

danger

Reddit requires authorization every time you go through their page.

danger

Only allows one callback URL per Client ID / Client Secret.

tip

This Provider template only has a one hour access token to it and only has the 'identity' scope. If you want to get a refresh token as well you must follow this:

```
    providers: [
      {
        id: "reddit",
        name: "Reddit",
        clientId: process.env.REDDIT_CLIENT_ID,
        clientSecret: process.env.REDDIT_CLIENT_SECRET,
        scope: "identity mysubreddits read", //Check Reddit API Documentation for more. The identity scope is required.
        type: "oauth",
        version: "2.0",
        params: { grant_type: "authorization_code" },
        accessTokenUrl: " https://www.reddit.com/api/v1/access_token",
        authorizationUrl:
          "https://www.reddit.com/api/v1/authorize?response_type=code&duration=permanent",
        profileUrl: "https://oauth.reddit.com/api/v1/me",
        profile: (profile) => {
          return {
            id: profile.id,
            name: profile.name,
            email: null,
          }
        },
      },
    ]

```
