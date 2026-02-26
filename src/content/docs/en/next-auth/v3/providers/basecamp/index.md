---
title: "Basecamp"
description: "The Basecamp Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/basecamp

# Basecamp | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/basecamp#documentation "Direct link to heading")

<https://github.com/basecamp/api/blob/master/sections/authentication.md>

## Configuration[​](https://next-auth.js.org/v3/providers/basecamp#configuration "Direct link to heading")

<https://launchpad.37signals.com/integrations>

## Options[​](https://next-auth.js.org/v3/providers/basecamp#options "Direct link to heading")

The **Basecamp Provider** comes with a set of default options:

- [Basecamp Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/basecamp.js)

You can override any of the options to suit your own use case.

## Examples[​](https://next-auth.js.org/v3/providers/basecamp#examples "Direct link to heading")

### Basic profile information[​](https://next-auth.js.org/v3/providers/basecamp#basic-profile-information "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Basecamp({
        clientId: process.env.BASECAMP_CLIENT_ID,
        clientSecret: process.env.BASECAMP_CLIENT_SECRET
      })
    ]
    ...

```

note

Using the example above, it is only possible to retrieve profile information such as account id, email and name. If you wish to retrieve user data in relation to a specific team, you must provide a different profileUrl and a custom function to handle profile information as shown in the example below.

### Profile information in relation to specific team[​](https://next-auth.js.org/v3/providers/basecamp#profile-information-in-relation-to-specific-team "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Basecamp({
        clientId: process.env.BASECAMP_CLIENT_ID,
        clientSecret: process.env.BASECAMP_CLIENT_SECRET,
        profileUrl: `https://3.basecampapi.com/${process.env.BASECAMP_TEAM_ID}/my/profile.json`,
        profile: (profile) => {
          return {
            id: profile.id,
            name: profile.name,
            email: profile.email_address,
            image: profile.avatar_url,
            admin: profile.admin,
            owner: profile.owner
          }
        }
      })
    ]
    ...

```

tip

The BASECAMP_TEAM_ID is found in the url path of your team's homepage. For example, if the url is `https://3.basecamp.com/1234567/projects`, then in this case the BASECAMP_TEAM_ID is [`1234567`](https://github.com/nextauthjs/next-auth/commit/1234567)
