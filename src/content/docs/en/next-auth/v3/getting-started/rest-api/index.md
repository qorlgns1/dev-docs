---
title: "REST API"
description: "NextAuth.js exposes a REST API which is used by the NextAuth.js client."
---

Source URL: https://next-auth.js.org/v3/getting-started/rest-api

# REST API | NextAuth.js

Version: v3

NextAuth.js exposes a REST API which is used by the NextAuth.js client.

#### `GET` /api/auth/signin[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthsignin "Direct link to heading")

Displays the sign in page.

#### `POST` /api/auth/signin/:provider[​](https://next-auth.js.org/v3/getting-started/rest-api#post-apiauthsigninprovider "Direct link to heading")

Starts an OAuth signin flow for the specified provider.

The POST submission requires CSRF token from `/api/auth/csrf`.

#### `GET` /api/auth/callback/:provider[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthcallbackprovider "Direct link to heading")

Handles returning requests from OAuth services during sign in.

For OAuth 2.0 providers that support the `state` option, the value of the `state` parameter is checked against the one that was generated when the sign in flow was started - this uses a hash of the CSRF token which MUST match for both the POST and `GET` calls during sign in.

#### `GET` /api/auth/signout[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthsignout "Direct link to heading")

Displays the sign out page.

#### `POST` /api/auth/signout[​](https://next-auth.js.org/v3/getting-started/rest-api#post-apiauthsignout "Direct link to heading")

Handles signing out - this is a `POST` submission to prevent malicious links from triggering signing a user out without their consent.

The `POST` submission requires CSRF token from `/api/auth/csrf`.

#### `GET` /api/auth/session[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthsession "Direct link to heading")

Returns client-safe session object - or an empty object if there is no session.

The contents of the session object that is returned are configurable with the session callback.

#### `GET` /api/auth/csrf[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthcsrf "Direct link to heading")

Returns object containing CSRF token. In NextAuth.js, CSRF protection is present on all authentication routes. It uses the "double submit cookie method", which uses a signed HttpOnly, host-only cookie.

The CSRF token returned by this endpoint must be passed as form variable named `csrfToken` in all `POST` submissions to any API endpoint.

#### `GET` /api/auth/providers[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthproviders "Direct link to heading")

Returns a list of configured OAuth services and details (e.g. sign in and callback URLs) for each service.

It can be used to dynamically generate custom sign up pages and to check what callback URLs are configured for each OAuth provider that is configured.

---

note

The default base path is `/api/auth` but it is configurable by specifying a custom path in `NEXTAUTH_URL`

e.g.

`NEXTAUTH_URL=https://example.com/myapp/api/authentication`

`/api/auth/signin` -> `/myapp/api/authentication/signin`
