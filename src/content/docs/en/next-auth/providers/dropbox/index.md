---
title: "Dropbox"
description: "The Dropbox Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/dropbox

# Dropbox | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/dropbox#documentation "Direct link to heading")

<https://developers.dropbox.com/oauth-guide>

## Configuration[​](https://next-auth.js.org/providers/dropbox#configuration "Direct link to heading")

<https://www.dropbox.com/developers/apps>

## Options[​](https://next-auth.js.org/providers/dropbox#options "Direct link to heading")

The **Dropbox Provider** comes with a set of default options:

- [Dropbox Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/dropbox.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/dropbox#example "Direct link to heading")

```
    import DropboxProvider from "next-auth/providers/dropbox";
    ...
    providers: [
      DropboxProvider({
        clientId: process.env.DROPBOX_CLIENT_ID,
        clientSecret: process.env.DROPBOX_CLIENT_SECRET
      })
    ]
    ...

```
