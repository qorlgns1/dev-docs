---
title: "Refresh Token Rotation"
description: "While NextAuth.js doesn't automatically handle access token rotation for OAuth providers yet, this functionality can be implemented using callbacks."
---

Source URL: https://next-auth.js.org/v3/tutorials/refresh-token-rotation

# Refresh Token Rotation | NextAuth.js

Version: v3

While NextAuth.js doesn't automatically handle access token rotation for OAuth providers yet, this functionality can be implemented using [callbacks](https://next-auth.js.org/configuration/callbacks).

## Source Code[​](https://next-auth.js.org/v3/tutorials/refresh-token-rotation#source-code "Direct link to heading")

_A working example can be accessed[here](https://github.com/lawrencecchen/next-auth-refresh-tokens)._

## Implementation[​](https://next-auth.js.org/v3/tutorials/refresh-token-rotation#implementation "Direct link to heading")

### Server Side[​](https://next-auth.js.org/v3/tutorials/refresh-token-rotation#server-side "Direct link to heading")

Using a [JWT callback](https://next-auth.js.org/configuration/callbacks#jwt-callback) and a [session callback](https://next-auth.js.org/configuration/callbacks#session-callback), we can persist OAuth tokens and refresh them when they expire.

Below is a sample implementation using Google's Identity Provider. Please note that the OAuth 2.0 request in the `refreshAccessToken()` function will vary between different providers, but the core logic should remain similar.

pages/api/auth/[...nextauth].js

```
    import NextAuth from "next-auth"
    import Providers from "next-auth/providers"

    const GOOGLE_AUTHORIZATION_URL =
      "https://accounts.google.com/o/oauth2/v2/auth?" +
      new URLSearchParams({
        prompt: "consent",
        access_type: "offline",
        response_type: "code",
      })

    /**
     * Takes a token, and returns a new token with updated
     * `accessToken` and `accessTokenExpires`. If an error occurs,
     * returns the old token and an error property
     */
    async function refreshAccessToken(token) {
      try {
        const url =
          "https://oauth2.googleapis.com/token?" +
          new URLSearchParams({
            client_id: process.env.GOOGLE_CLIENT_ID,
            client_secret: process.env.GOOGLE_CLIENT_SECRET,
            grant_type: "refresh_token",
            refresh_token: token.refreshToken,
          })

        const response = await fetch(url, {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          method: "POST",
        })

        const refreshedTokens = await response.json()

        if (!response.ok) {
          throw refreshedTokens
        }

        return {
          ...token,
          accessToken: refreshedTokens.access_token,
          accessTokenExpires: Date.now() + refreshedTokens.expires_in * 1000,
          refreshToken: refreshedTokens.refresh_token ?? token.refreshToken, // Fall back to old refresh token
        }
      } catch (error) {
        console.log(error)

        return {
          ...token,
          error: "RefreshAccessTokenError",
        }
      }
    }

    export default NextAuth({
      providers: [
        Providers.Google({
          clientId: process.env.GOOGLE_CLIENT_ID,
          clientSecret: process.env.GOOGLE_CLIENT_SECRET,
          authorizationUrl: GOOGLE_AUTHORIZATION_URL,
        }),
      ],
      callbacks: {
        async jwt(token, user, account) {
          // Initial sign in
          if (account && user) {
            return {
              accessToken: account.accessToken,
              accessTokenExpires: Date.now() + account.expires_in * 1000,
              refreshToken: account.refresh_token,
              user,
            }
          }

          // Return previous token if the access token has not expired yet
          if (Date.now() < token.accessTokenExpires) {
            return token
          }

          // Access token has expired, try to update it
          return refreshAccessToken(token)
        },
        async session(session, token) {
          if (token) {
            session.user = token.user
            session.accessToken = token.accessToken
            session.error = token.error
          }

          return session
        },
      },
    })

```

### Client Side[​](https://next-auth.js.org/v3/tutorials/refresh-token-rotation#client-side "Direct link to heading")

The `RefreshAccessTokenError` error that is caught in the `refreshAccessToken()` method is passed all the way to the client. This means that you can direct the user to the sign in flow if we cannot refresh their token.

We can handle this functionality as a side effect:

pages/index.js

```
    import { signIn, useSession } from "next-auth/client";
    import { useEffect } from "react";

    const HomePage() {
      const [session] = useSession();

      useEffect(() => {
        if (session?.error === "RefreshAccessTokenError") {
          signIn(); // Force sign in to hopefully resolve error
        }
      }, [session]);

    return (...)
    }

```
