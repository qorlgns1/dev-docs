---
title: "LinkedIn"
description: "From the Auth tab get the client ID and client secret. On the same tab, add redirect URLs such as http://localhost:3000/api/auth/callback/linkedin so ..."
---

Source URL: https://next-auth.js.org/v3/providers/linkedin

# LinkedIn | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/linkedin#documentation "Direct link to heading")

<https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow>

## Configuration[​](https://next-auth.js.org/v3/providers/linkedin#configuration "Direct link to heading")

<https://www.linkedin.com/developers/apps/>

From the Auth tab get the client ID and client secret. On the same tab, add redirect URLs such as http://localhost:3000/api/auth/callback/linkedin so LinkedIn can correctly redirect back to your application. Finally, head over to the Products tab and enable the "Sign In with LinkedIn" product. The LinkedIn team will review and approve your request before you can test it out.

![image](https://user-images.githubusercontent.com/330396/114429603-68195600-9b72-11eb-8311-62e58383c42b.png)

## Options[​](https://next-auth.js.org/v3/providers/linkedin#options "Direct link to heading")

The **LinkedIn Provider** comes with a set of default options:

- [LinkedIn Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/linkedin.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/linkedin#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.LinkedIn({
        clientId: process.env.LINKEDIN_CLIENT_ID,
        clientSecret: process.env.LINKEDIN_CLIENT_SECRET
      })
    ]
    ...

```
