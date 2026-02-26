---
title: "Introduction"
description: "NextAuth.js is a complete open source authentication solution for Next.js applications."
---

Source URL: https://next-auth.js.org/v3/getting-started/introduction

# Introduction | NextAuth.js

Version: v3

## About NextAuth.js[​](https://next-auth.js.org/v3/getting-started/introduction#about-nextauthjs "Direct link to heading")

NextAuth.js is a complete open source authentication solution for [Next.js](http://nextjs.org/) applications.

It is designed from the ground up to support Next.js and Serverless.

[Check out the example code](https://next-auth.js.org/getting-started/example) to see how easy it is to use NextAuth.js for authentication.

### Flexible and easy to use[​](https://next-auth.js.org/v3/getting-started/introduction#flexible-and-easy-to-use "Direct link to heading")

- Designed to work with any OAuth service, it supports OAuth 1.0, 1.0A and 2.0
- Built-in support for [many popular sign-in services](https://next-auth.js.org/configuration/providers/oauth)
- Supports email / passwordless authentication
- Supports stateless authentication with any backend (Active Directory, LDAP, etc)
- Supports both JSON Web Tokens and database sessions
- Designed for Serverless but runs anywhere (AWS Lambda, Docker, Heroku, etc…)

### Own your own data[​](https://next-auth.js.org/v3/getting-started/introduction#own-your-own-data "Direct link to heading")

NextAuth.js can be used with or without a database.

- An open source solution that allows you to keep control of your data
- Supports Bring Your Own Database (BYOD) and can be used with any database
- Built-in support for [MySQL, MariaDB, Postgres, SQL Server, MongoDB and SQLite](https://next-auth.js.org/configuration/databases)
- Works great with databases from popular hosting providers
- Can also be used _without a database_ (e.g. OAuth + JWT)

_Note: Email sign in requires a database to be configured to store single-use verification tokens._

### Secure by default[​](https://next-auth.js.org/v3/getting-started/introduction#secure-by-default "Direct link to heading")

- Promotes the use of passwordless sign in mechanisms
- Designed to be secure by default and encourage best practice for safeguarding user data
- Uses Cross Site Request Forgery Tokens on POST routes (sign in, sign out)
- Default cookie policy aims for the most restrictive policy appropriate for each cookie
- When JSON Web Tokens are enabled, they are signed by default (JWS) with HS512
- Use JWT encryption (JWE) by setting the option `encryption: true` (defaults to A256GCM)
- Auto-generates symmetric signing and encryption keys for developer convenience
- Features tab/window syncing and keepalive messages to support short lived sessions
- Attempts to implement the latest guidance published by [Open Web Application Security Project](https://owasp.org/)

Advanced options allow you to define your own routines to handle controlling what accounts are allowed to sign in, for encoding and decoding JSON Web Tokens and to set custom cookie security policies and session properties, so you can control who is able to sign in and how often sessions have to be re-validated.

## Credits[​](https://next-auth.js.org/v3/getting-started/introduction#credits "Direct link to heading")

NextAuth.js is an open source project that is only possible [thanks to contributors](https://next-auth.js.org/contributors).

## Getting Started[​](https://next-auth.js.org/v3/getting-started/introduction#getting-started "Direct link to heading")

[Check out the example code](https://next-auth.js.org/getting-started/example) to see how easy it is to use NextAuth.js for authentication.
