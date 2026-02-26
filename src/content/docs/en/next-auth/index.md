---
title: "NextAuth.js"
description: "_(Google, Facebook, Auth0, Apple…)_"
---

Source URL: https://next-auth.js.org/

# NextAuth.js

## Open Source. Full Stack. Own Your Data.

![Easy](https://next-auth.js.org/img/undraw_social.svg)

### Easy

- Built in support for popular services
  _(Google, Facebook, Auth0, Apple…)_
- Built in email / passwordless / magic link
- Use with any username / password store
- Use with OAuth 1.0 & 2.0 services

![Flexible](https://next-auth.js.org/img/undraw_authentication.svg)

### Flexible

- Built for Serverless, runs anywhere
- Bring Your Own Database - or none!
  _(MySQL, Postgres, MSSQL, MongoDB…)_
- Choose database sessions or JWT
- Secure web pages and API routes

![Secure](https://next-auth.js.org/img/undraw_secure.svg)

### Secure

- Signed, prefixed, server-only cookies
- HTTP POST + CSRF Token validation
- JWT with JWS / JWE / JWK
- Tab syncing, auto-revalidation, keepalives
- Doesn't rely on client side JavaScript

[npm install next-auth](https://www.npmjs.com/package/next-auth)

## Add authentication in minutes!

#### Server /pages/api/auth/[...nextauth].js

```
    import NextAuth from 'next-auth'
    import AppleProvider from 'next-auth/providers/apple'
    import FacebookProvider from 'next-auth/providers/facebook'
    import GoogleProvider from 'next-auth/providers/google'
    import EmailProvider from 'next-auth/providers/email'

    export default NextAuth({
      providers: [
        // OAuth authentication providers...
        AppleProvider({
          clientId: process.env.APPLE_ID,
          clientSecret: process.env.APPLE_SECRET
        }),
        FacebookProvider({
          clientId: process.env.FACEBOOK_ID,
          clientSecret: process.env.FACEBOOK_SECRET
        }),
        GoogleProvider({
          clientId: process.env.GOOGLE_ID,
          clientSecret: process.env.GOOGLE_SECRET
        }),
        // Passwordless / email sign in
        EmailProvider({
          server: process.env.MAIL_SERVER,
          from: 'NextAuth.js <no-reply@example.com>'
        }),
      ]
    })

```

#### Client (App) /pages/\_app.jsx

```
    import { SessionProvider } from "next-auth/react"

    export default function App({
      Component, pageProps: { session, ...pageProps }
    }) {
      return (
      )
    }

```

#### Client (Page) /pages/index.js

```
    import { useSession, signIn, signOut } from "next-auth/react"

    export default function Component() {
      const { data: session } = useSession()
      if(session) {
        return <>
          Signed in as {session.user.email} <br/>
          <button onClick={() => signOut()}>Sign out</button>
        </>
      }
      return <>
        Not signed in <br/>
        <button onClick={() => signIn()}>Sign in</button>
      </>
    }

```

[Example Code](https://next-auth.js.org/getting-started/example)

NextAuth.js is an open source community project.
