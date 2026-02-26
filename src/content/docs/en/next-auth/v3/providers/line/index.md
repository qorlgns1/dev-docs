---
title: "LINE"
description: "The Line Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/line

# LINE | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/line#documentation "Direct link to heading")

<https://developers.line.biz/en/docs/line-login/integrate-line-login/>

## Configuration[​](https://next-auth.js.org/v3/providers/line#configuration "Direct link to heading")

<https://developers.line.biz/console/>

## Options[​](https://next-auth.js.org/v3/providers/line#options "Direct link to heading")

The **Line Provider** comes with a set of default options:

- [Line Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/line.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/line#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.LINE({
        clientId: process.env.LINE_CLIENT_ID,
        clientSecret: process.env.LINE_CLIENT_SECRET
      })
    ]
    ...

```

## Instructions[​](https://next-auth.js.org/v3/providers/line#instructions "Direct link to heading")

### Configuration[​](https://next-auth.js.org/v3/providers/line#configuration-1 "Direct link to heading")

Create a provider and a LINE login channel at `https://developers.line.biz/console/`. In the settings of the channel under LINE Login, activate web app and configure the following:

- Callback URL
  - http://localhost:3000/api/auth/callback/line
