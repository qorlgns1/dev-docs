---
title: "FaunaDB"
description: "원본 URL: https://next-auth.js.org/v3/adapters/fauna"
---

원본 URL: https://next-auth.js.org/v3/adapters/fauna

버전: v3

# FaunaDB

이것은 [`next-auth`](https://next-auth.js.org)용 Fauna 어댑터입니다. 이 패키지는 기본 `next-auth` 패키지와 함께 사용할 때만 사용할 수 있습니다. 독립형 패키지가 아닙니다.

Fauna 스키마와 시드 정보는 [next-auth.js.org/adapters/fauna](https://next-auth.js.org/adapters/fauna) 문서에서 확인할 수 있습니다.

## 시작하기[​](https://next-auth.js.org/v3/adapters/fauna#getting-started "Direct link to heading")

1. `next-auth`와 `@next-auth/fauna-adapter@canary`를 설치하세요

```
    npm install next-auth @next-auth/fauna-adapter@canary

```

2. 이 어댑터를 `pages/api/auth/[...nextauth].js`의 next-auth 구성 객체에 추가하세요.

pages/api/auth/[...nextauth].js

```
    import NextAuth from "next-auth"
    import Providers from "next-auth/providers"
    import * as Fauna from "faunadb"
    import { FaunaAdapter } from "@next-auth/fauna-adapter"

    const client = new Fauna.Client({
      secret: "secret",
      scheme: "http",
      domain: "localhost",
      port: 8443,
    })

    // For more information on each option (and a full list of options) go to
    // https://next-auth.js.org/configuration/options
    export default NextAuth({
      // https://providers.authjs.dev
      providers: [
        Providers.Google({
          clientId: process.env.GOOGLE_ID,
          clientSecret: process.env.GOOGLE_SECRET,
        }),
      ],
      adapter: FaunaAdapter({ faunaClient: client})
      ...
    })

```

## 스키마[​](https://next-auth.js.org/v3/adapters/fauna#schema "Direct link to heading")

```
    CreateCollection({ name: "accounts" })
    CreateCollection({ name: "sessions" })
    CreateCollection({ name: "users" })
    CreateCollection({ name: "verification_requests" })
    CreateIndex({
      name: "account_by_provider_account_id",
      source: Collection("accounts"),
      unique: true,
      terms: [
        { field: ["data", "providerId"] },
        { field: ["data", "providerAccountId"] },
      ],
    })
    CreateIndex({
      name: "session_by_token",
      source: Collection("sessions"),
      unique: true,
      terms: [{ field: ["data", "sessionToken"] }],
    })
    CreateIndex({
      name: "user_by_email",
      source: Collection("users"),
      unique: true,
      terms: [{ field: ["data", "email"] }],
    })
    CreateIndex({
      name: "verification_request_by_token",
      source: Collection("verification_requests"),
      unique: true,
      terms: [{ field: ["data", "token"] }, { field: ["data", "identifier"] }],
    })

```
