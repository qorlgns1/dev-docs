---
title: "Warnings"
description: "This is a list of warning output from NextAuth.js."
---

Source URL: https://next-auth.js.org/warnings

# Warnings | NextAuth.js

Version: v4

This is a list of warning output from NextAuth.js.

All warnings indicate things which you should take a look at, but do not inhibit normal operation.

---

## Client[​](https://next-auth.js.org/warnings#client "Direct link to heading")

#### NEXTAUTH_URL[​](https://next-auth.js.org/warnings#nextauth_url "Direct link to heading")

Environment variable `NEXTAUTH_URL` missing. Please set it in your `.env` file.

note

On [Vercel](https://vercel.com) deployments, we will read the `VERCEL_URL` environment variable, so you won't need to define `NEXTAUTH_URL`.

---

## Server[​](https://next-auth.js.org/warnings#server "Direct link to heading")

These warnings are displayed on the terminal.

#### NO_SECRET[​](https://next-auth.js.org/warnings#no_secret "Direct link to heading")

In development, we generate a `secret` based on your configuration for convenience. This is volatile and will throw an error in production. [Read more](https://next-auth.js.org/configuration/options#secret)

#### TWITTER_OAUTH_2_BETA[​](https://next-auth.js.org/warnings#twitter_oauth_2_beta "Direct link to heading")

Twitter OAuth 2.0 is currently in beta as certain changes might still be necessary. This is not covered by semver. See the docs <https://next-auth.js.org/providers/twitter#oauth-2>

#### EXPERIMENTAL_API[​](https://next-auth.js.org/warnings#experimental_api "Direct link to heading")

Some APIs are still experimental; they may be changed or removed in the future. Use at your own risk.

#### DEBUG_ENABLED[​](https://next-auth.js.org/warnings#debug_enabled "Direct link to heading")

You have enabled the `debug` option. It is meant for development only, to help you catch issues in your authentication flow and you should consider removing this option when deploying to production. One way of only allowing debugging while not in production is to set `debug: process.env.NODE_ENV !== "production"`, so you can commit this without needing to change the value.

If you want to log debug messages during production anyway, we recommend setting the [`logger` option](https://next-auth.js.org/configuration/options#logger) with proper sanitization of potentially sensitive user information.

## Adapter[​](https://next-auth.js.org/warnings#adapter "Direct link to heading")

### ADAPTER_TYPEORM_UPDATING_ENTITIES[​](https://next-auth.js.org/warnings#adapter_typeorm_updating_entities "Direct link to heading")

This warning occurs when typeorm finds that the provided entities differ from the database entities. By default while not in `production` the typeorm adapter will always synchronize changes made to the entities codefiles.

Disable this warning by setting `synchronize: false` in your typeorm config

Example:

/pages/api/auth/[...nextauth].js

```
    adapter: TypeORMLegacyAdapter({
      type: 'mysql',
      username: process.env.DATABASE_USERNAME,
      password: process.env.DATABASE_PASSWORD,
      host: process.env.DATABASE_HOST,
      database: process.env.DATABASE_DB,
      synchronize: false
    }),

```
