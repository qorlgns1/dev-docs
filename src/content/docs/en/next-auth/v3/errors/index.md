---
title: "Errors"
description: "This is a list of errors output from NextAuth.js."
---

Source URL: https://next-auth.js.org/v3/errors

# Errors | NextAuth.js

Version: v3

This is a list of errors output from NextAuth.js.

All errors indicate an unexpected problem, you should not expect to see errors.

If you are seeing any of these errors in the console, something is wrong.

---

## Client[​](https://next-auth.js.org/v3/errors#client "Direct link to heading")

These errors are returned from the client. As the client is [Universal JavaScript (or "Isomorphic JavaScript")](https://en.wikipedia.org/wiki/Isomorphic_JavaScript) it can be run on the client or server, so these errors can occur in both in the terminal and in the browser console.

#### CLIENT_USE_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#client_use_session_error "Direct link to heading")

This error occurs when the `useSession()` React Hook has a problem fetching session data.

#### CLIENT_FETCH_ERROR[​](https://next-auth.js.org/v3/errors#client_fetch_error "Direct link to heading")

If you see `CLIENT_FETCH_ERROR` make sure you have configured the `NEXTAUTH_URL` environment variable.

---

## Server[​](https://next-auth.js.org/v3/errors#server "Direct link to heading")

These errors are displayed on the terminal.

### OAuth[​](https://next-auth.js.org/v3/errors#oauth "Direct link to heading")

#### OAUTH_GET_ACCESS_TOKEN_ERROR[​](https://next-auth.js.org/v3/errors#oauth_get_access_token_error "Direct link to heading")

#### OAUTH_V1_GET_ACCESS_TOKEN_ERROR[​](https://next-auth.js.org/v3/errors#oauth_v1_get_access_token_error "Direct link to heading")

#### OAUTH_GET_PROFILE_ERROR[​](https://next-auth.js.org/v3/errors#oauth_get_profile_error "Direct link to heading")

#### OAUTH_PARSE_PROFILE_ERROR[​](https://next-auth.js.org/v3/errors#oauth_parse_profile_error "Direct link to heading")

#### OAUTH_CALLBACK_HANDLER_ERROR[​](https://next-auth.js.org/v3/errors#oauth_callback_handler_error "Direct link to heading")

---

### Signin / Callback[​](https://next-auth.js.org/v3/errors#signin--callback "Direct link to heading")

#### GET_AUTHORIZATION_URL_ERROR[​](https://next-auth.js.org/v3/errors#get_authorization_url_error "Direct link to heading")

#### SIGNIN_OAUTH_ERROR[​](https://next-auth.js.org/v3/errors#signin_oauth_error "Direct link to heading")

#### CALLBACK_OAUTH_ERROR[​](https://next-auth.js.org/v3/errors#callback_oauth_error "Direct link to heading")

#### SIGNIN_EMAIL_ERROR[​](https://next-auth.js.org/v3/errors#signin_email_error "Direct link to heading")

#### CALLBACK_EMAIL_ERROR[​](https://next-auth.js.org/v3/errors#callback_email_error "Direct link to heading")

#### EMAIL_REQUIRES_ADAPTER_ERROR[​](https://next-auth.js.org/v3/errors#email_requires_adapter_error "Direct link to heading")

The Email authentication provider can only be used if a database is configured.

#### CALLBACK_CREDENTIALS_JWT_ERROR[​](https://next-auth.js.org/v3/errors#callback_credentials_jwt_error "Direct link to heading")

The Credentials Provider can only be used if JSON Web Tokens are used for sessions.

JSON Web Tokens are used for Sessions by default if you have not specified a database. However if you are using a database, then Database Sessions are enabled by default and you need to [explicitly enable JWT Sessions](https://next-auth.js.org/configuration/options#session) to use the Credentials Provider.

If you are using a Credentials Provider, NextAuth.js will not persist users or sessions in a database - user accounts used with the Credentials Provider must be created and managed outside of NextAuth.js.

In _most cases_ it does not make sense to specify a database in NextAuth.js options and support a Credentials Provider.

#### CALLBACK_CREDENTIALS_HANDLER_ERROR[​](https://next-auth.js.org/v3/errors#callback_credentials_handler_error "Direct link to heading")

#### PKCE_ERROR[​](https://next-auth.js.org/v3/errors#pkce_error "Direct link to heading")

The provider you tried to use failed when setting [PKCE or Proof Key for Code Exchange](https://tools.ietf.org/html/rfc7636#section-4.2). The `code_verifier` is saved in a cookie called (by default) `__Secure-next-auth.pkce.code_verifier` which expires after 15 minutes. Check if `cookies.pkceCodeVerifier` is configured correctly. The default `code_challenge_method` is `"S256"`. This is currently not configurable to `"plain"`, as it is not recommended, and in most cases it is only supported for backward compatibility.

---

### Session Handling[​](https://next-auth.js.org/v3/errors#session-handling "Direct link to heading")

#### JWT_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#jwt_session_error "Direct link to heading")

<https://next-auth.js.org/errors#jwt_session_error> JWKKeySupport: the key does not support HS512 verify algorithm

The algorithm used for generating your key isn't listed as supported. You can generate a HS512 key using

```
      jose newkey -s 512 -t oct -a HS512

```

If you are unable to use an HS512 key (for example to interoperate with other services) you can define what is supported using

```
      jwt: {
        signingKey: {"kty":"oct","kid":"--","alg":"HS256","k":"--"},
        verificationOptions: {
          algorithms: ["HS256"]
        }
      }

```

#### SESSION_ERROR[​](https://next-auth.js.org/v3/errors#session_error "Direct link to heading")

---

### Signout[​](https://next-auth.js.org/v3/errors#signout "Direct link to heading")

#### SIGNOUT_ERROR[​](https://next-auth.js.org/v3/errors#signout_error "Direct link to heading")

---

### Database[​](https://next-auth.js.org/v3/errors#database "Direct link to heading")

These errors are logged by the TypeORM Adapter, which is the default database adapter.

They all indicate a problem interacting with the database.

#### ADAPTER_CONNECTION_ERROR[​](https://next-auth.js.org/v3/errors#adapter_connection_error "Direct link to heading")

#### CREATE_USER_ERROR[​](https://next-auth.js.org/v3/errors#create_user_error "Direct link to heading")

#### GET_USER_BY_ID_ERROR[​](https://next-auth.js.org/v3/errors#get_user_by_id_error "Direct link to heading")

#### GET_USER_BY_EMAIL_ERROR[​](https://next-auth.js.org/v3/errors#get_user_by_email_error "Direct link to heading")

#### GET_USER_BY_PROVIDER_ACCOUNT_ID_ERROR[​](https://next-auth.js.org/v3/errors#get_user_by_provider_account_id_error "Direct link to heading")

#### LINK_ACCOUNT_ERROR[​](https://next-auth.js.org/v3/errors#link_account_error "Direct link to heading")

#### CREATE_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#create_session_error "Direct link to heading")

#### GET_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#get_session_error "Direct link to heading")

#### UPDATE_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#update_session_error "Direct link to heading")

#### DELETE_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#delete_session_error "Direct link to heading")

#### CREATE_VERIFICATION_REQUEST_ERROR[​](https://next-auth.js.org/v3/errors#create_verification_request_error "Direct link to heading")

#### GET_VERIFICATION_REQUEST_ERROR[​](https://next-auth.js.org/v3/errors#get_verification_request_error "Direct link to heading")

#### DELETE_VERIFICATION_REQUEST_ERROR[​](https://next-auth.js.org/v3/errors#delete_verification_request_error "Direct link to heading")

---

### Other[​](https://next-auth.js.org/v3/errors#other "Direct link to heading")

#### SEND_VERIFICATION_EMAIL_ERROR[​](https://next-auth.js.org/v3/errors#send_verification_email_error "Direct link to heading")

This error occurs when the Email Authentication Provider is unable to send an email.

Check your mail server configuration.

#### MISSING_NEXTAUTH_API_ROUTE_ERROR[​](https://next-auth.js.org/v3/errors#missing_nextauth_api_route_error "Direct link to heading")

This error happens when `[...nextauth].js` file is not found inside `pages/api/auth`.

Make sure the file is there and the filename is written correctly.
