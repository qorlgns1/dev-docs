---
title: "Warnings"
description: "This is a list of warning output from NextAuth.js."
---

Source URL: https://next-auth.js.org/v3/warnings

# Warnings | NextAuth.js

Version: v3

This is a list of warning output from NextAuth.js.

All warnings indicate things which you should take a look at, but do not inhibit normal operation.

---

## Client[​](https://next-auth.js.org/v3/warnings#client "Direct link to heading")

#### NEXTAUTH_URL[​](https://next-auth.js.org/v3/warnings#nextauth_url "Direct link to heading")

Environment variable `NEXTAUTH_URL` missing. Please set it in your `.env` file.

---

## Server[​](https://next-auth.js.org/v3/warnings#server "Direct link to heading")

These warnings are displayed on the terminal.

#### JWT_AUTO_GENERATED_SIGNING_KEY[​](https://next-auth.js.org/v3/warnings#jwt_auto_generated_signing_key "Direct link to heading")

To remedy this warning, you can either:

**Option 1** : Pass a pre-regenerated Private Key (and, optionally a Public Key) in the jwt options.

/pages/api/auth/[...nextauth].js

```
    jwt: {
      signingKey: process.env.JWT_SIGNING_PRIVATE_KEY,

      // You can also specify a public key for verification if using public/private key (but private only is fine)
      // verificationKey: process.env.JWT_SIGNING_PUBLIC_KEY,

      // If you want to use some key format other than HS512 you can specify custom options to use
      // when verifying (note: verificationOptions should include a value for maxTokenAge as well).
      // verificationOptions = {
      //   maxTokenAge: `${maxAge}s`, // e.g. `${30 * 24 * 60 * 60}s` = 30 days
      //   algorithms: ['HS512']
      // },
    }

```

You can use [node-jose-tools](https://www.npmjs.com/package/node-jose-tools) to generate keys on the command line and set them as environment variables, i.e. `jose newkey -s 256 -t oct -a HS512`.

**Option 2** : Specify custom encode/decode functions on the jwt object. This gives you complete control over signing / verification / etc.

#### JWT_AUTO_GENERATED_ENCRYPTION_KEY[​](https://next-auth.js.org/v3/warnings#jwt_auto_generated_encryption_key "Direct link to heading")

#### SIGNIN_CALLBACK_REJECT_REDIRECT[​](https://next-auth.js.org/v3/warnings#signin_callback_reject_redirect "Direct link to heading")

You returned something in the `signIn` callback, that is being deprecated.

You probably had something similar in the callback:

```
    return Promise.reject("/some/url")

```

or

```
    throw "/some/url"

```

To remedy this, simply return the url instead:

```
    return "/some/url"

```

#### STATE_OPTION_DEPRECATION[​](https://next-auth.js.org/v3/warnings#state_option_deprecation "Direct link to heading")

You provided `state: true` or `state: false` as a provider option. This is being deprecated in a later release in favour of `protection: "state"` and `protection: "none"` respectively. To remedy this warning:

- If you use `state: true`, just simply remove it. The default is `protection: "state"` already..
- If you use `state: false`, set `protection: "none"`.
