---
title: "Refresh Token Rotation"
description: "NextAuth.js는 아직 OAuth provider의 access token rotation을 자동으로 처리하지 않지만, 이 기능은 callbacks를 사용해 구현할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/tutorials/refresh-token-rotation

# Refresh Token Rotation | NextAuth.js

버전: v3

NextAuth.js는 아직 OAuth provider의 access token rotation을 자동으로 처리하지 않지만, 이 기능은 [callbacks](https://next-auth.js.org/configuration/callbacks)를 사용해 구현할 수 있습니다.

## 소스 코드[​](https://next-auth.js.org/v3/tutorials/refresh-token-rotation#source-code "헤딩으로 바로 가는 링크")

_동작하는 예시는 [here](https://github.com/lawrencecchen/next-auth-refresh-tokens)에서 확인할 수 있습니다._

## 구현[​](https://next-auth.js.org/v3/tutorials/refresh-token-rotation#implementation "헤딩으로 바로 가는 링크")

### 서버 사이드[​](https://next-auth.js.org/v3/tutorials/refresh-token-rotation#server-side "헤딩으로 바로 가는 링크")

[JWT callback](https://next-auth.js.org/configuration/callbacks#jwt-callback)과 [session callback](https://next-auth.js.org/configuration/callbacks#session-callback)을 사용하면 OAuth 토큰을 유지하고 만료 시 갱신할 수 있습니다.

아래는 Google Identity Provider를 사용하는 샘플 구현입니다. `refreshAccessToken()` 함수의 OAuth 2.0 요청은 provider마다 달라질 수 있지만, 핵심 로직은 유사하게 유지됩니다.

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

### 클라이언트 사이드[​](https://next-auth.js.org/v3/tutorials/refresh-token-rotation#client-side "헤딩으로 바로 가는 링크")

`refreshAccessToken()` 메서드에서 잡힌 `RefreshAccessTokenError` 오류는 클라이언트까지 그대로 전달됩니다. 즉, 토큰을 갱신할 수 없는 경우 사용자를 sign in flow로 보낼 수 있습니다.

이 기능은 사이드 이펙트로 처리할 수 있습니다:

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
