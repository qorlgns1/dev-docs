---
title: 'Documentation[​](https://next-auth.js.org/v3/providers/vk#documentation "Direct link to heading")'
description: "The VK Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/vk

# VK | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/vk#documentation "Direct link to heading")

<https://vk.com/dev/first_guide>

## Configuration[​](https://next-auth.js.org/v3/providers/vk#configuration "Direct link to heading")

<https://vk.com/apps?act=manage>

## Options[​](https://next-auth.js.org/v3/providers/vk#options "Direct link to heading")

The **VK Provider** comes with a set of default options:

- [VK Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/vk.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/vk#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.VK({
        clientId: process.env.VK_CLIENT_ID,
        clientSecret: process.env.VK_CLIENT_SECRET
      })
    ]
    ...

```

note

By default the provider uses `5.126` version of the API. See <https://vk.com/dev/versions> for more info.

If you want to use a different version, you can pass it to provider's options object:

```
    // pages/api/auth/[...nextauth].js

    const apiVersion = "5.126"
    ...
    providers: [
      Providers.VK({
        accessTokenUrl: `https://oauth.vk.com/access_token?v=${apiVersion}`,
        requestTokenUrl: `https://oauth.vk.com/access_token?v=${apiVersion}`,
        authorizationUrl:
          `https://oauth.vk.com/authorize?response_type=code&v=${apiVersion}`,
        profileUrl: `https://api.vk.com/method/users.get?fields=photo_100&v=${apiVersion}`,
      })
    ]
    ...

```
