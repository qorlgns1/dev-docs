---
title: "Providers"
description: "Authentication Providers in NextAuth.js are services that can be used to sign in a user."
---

Source URL: https://next-auth.js.org/v3/configuration/providers

# Providers | NextAuth.js

Version: v3

Authentication Providers in **NextAuth.js** are services that can be used to sign in a user.

There's four ways a user can be signed in:

- [Using a built-in OAuth Provider](https://next-auth.js.org/v3/configuration/providers#oauth-providers) (e.g Github, Twitter, Google, etc...)
- [Using a custom OAuth Provider](https://next-auth.js.org/v3/configuration/providers#using-a-custom-provider)
- [Using Email](https://next-auth.js.org/v3/configuration/providers#email-provider)
- [Using Credentials](https://next-auth.js.org/v3/configuration/providers#credentials-provider)

note

NextAuth.js is designed to work with any OAuth service, it supports **OAuth 1.0** , **1.0A** and **2.0** and has built-in support for most popular sign-in services.

## OAuth Providers[​](https://next-auth.js.org/v3/configuration/providers#oauth-providers "Direct link to heading")

### Available providers[​](https://next-auth.js.org/v3/configuration/providers#available-providers "Direct link to heading")

[42 School](https://next-auth.js.org/providers/42-school),[Amazon Cognito](https://next-auth.js.org/providers/cognito),[Apple](https://next-auth.js.org/providers/apple),[Atlassian](https://next-auth.js.org/providers/atlassian),[Auth0](https://next-auth.js.org/providers/auth0),[Authentik](https://next-auth.js.org/providers/authentik),[Azure Active Directory](https://next-auth.js.org/providers/azure-ad),[Azure Active Directory B2C](https://next-auth.js.org/providers/azure-ad-b2c),[Battle.net](https://next-auth.js.org/providers/battle.net),[Box](https://next-auth.js.org/providers/box),[BoxyHQ SAML](https://next-auth.js.org/providers/boxyhq-saml),[Bungie](https://next-auth.js.org/providers/bungie),[Coinbase](https://next-auth.js.org/providers/coinbase),[Discord](https://next-auth.js.org/providers/discord),[Dropbox](https://next-auth.js.org/providers/dropbox),[DuendeIdentityServer6](https://next-auth.js.org/providers/duende-identityserver6),[EVE Online](https://next-auth.js.org/providers/eveonline),[Facebook](https://next-auth.js.org/providers/facebook),[FACEIT](https://next-auth.js.org/providers/faceit),[Foursquare](https://next-auth.js.org/providers/foursquare),[Freshbooks](https://next-auth.js.org/providers/freshbooks),[FusionAuth](https://next-auth.js.org/providers/fusionauth),[GitHub](https://next-auth.js.org/providers/github),[GitLab](https://next-auth.js.org/providers/gitlab),[Google](https://next-auth.js.org/providers/google),[HubSpot](https://next-auth.js.org/providers/hubspot),[IdentityServer4](https://next-auth.js.org/providers/identity-server4),[Instagram](https://next-auth.js.org/providers/instagram),[Kakao](https://next-auth.js.org/providers/kakao),[Keycloak](https://next-auth.js.org/providers/keycloak),[LINE](https://next-auth.js.org/providers/line),[LinkedIn](https://next-auth.js.org/providers/linkedin),[Mail.ru](https://next-auth.js.org/providers/mailru),[Mailchimp](https://next-auth.js.org/providers/mailchimp),[Medium](https://next-auth.js.org/providers/medium),[Naver](https://next-auth.js.org/providers/naver),[Netlify](https://next-auth.js.org/providers/netlify),[Okta](https://next-auth.js.org/providers/okta),[OneLogin](https://next-auth.js.org/providers/onelogin),[Osso](https://next-auth.js.org/providers/osso),[osu!](https://next-auth.js.org/providers/osu),[Patreon](https://next-auth.js.org/providers/patreon),[Pinterest](https://next-auth.js.org/providers/pinterest),[Pipedrive](https://next-auth.js.org/providers/pipedrive),[Reddit](https://next-auth.js.org/providers/reddit),[Salesforce](https://next-auth.js.org/providers/salesforce),[Slack](https://next-auth.js.org/providers/slack),[Spotify](https://next-auth.js.org/providers/spotify),[Strava](https://next-auth.js.org/providers/strava),[Todoist](https://next-auth.js.org/providers/todoist),[Trakt](https://next-auth.js.org/providers/trakt),[Twitch](https://next-auth.js.org/providers/twitch),[Twitter](https://next-auth.js.org/providers/twitter),[United Effects](https://next-auth.js.org/providers/united-effects),[VK](https://next-auth.js.org/providers/vk),[Wikimedia](https://next-auth.js.org/providers/wikimedia),[WordPress.com](https://next-auth.js.org/providers/wordpress),[WorkOS](https://next-auth.js.org/providers/workos),[Yandex](https://next-auth.js.org/providers/yandex),[Zitadel](https://next-auth.js.org/providers/zitadel),[Zoho](https://next-auth.js.org/providers/zoho),[Zoom](https://next-auth.js.org/providers/zoom),

### How to[​](https://next-auth.js.org/v3/configuration/providers#how-to "Direct link to heading")

1. Register your application at the developer portal of your provider. There are links above to the developer docs for most supported providers with details on how to register your application.

2. The redirect URI should follow this format:

```
    [origin]/api/auth/callback/[provider]

```

For example, Twitter on `localhost` this would be:

```
    http://localhost:3000/api/auth/callback/twitter

```

3. Create a `.env` file at the root of your project and add the client ID and client secret. For Twitter this would be:

```
    TWITTER_ID=YOUR_TWITTER_CLIENT_ID
    TWITTER_SECRET=YOUR_TWITTER_CLIENT_SECRET

```

4. Now you can add the provider settings to the NextAuth.js options object. You can add as many OAuth providers as you like, as you can see `providers` is an array.

pages/api/auth/[...nextauth].js

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Twitter({
        clientId: process.env.TWITTER_ID,
        clientSecret: process.env.TWITTER_SECRET
      })
    ],
    ...

```

5. Once a provider has been setup, you can sign in at the following URL: `[origin]/api/auth/signin`. This is an unbranded auto-generated page with all the configured providers.

### Options[​](https://next-auth.js.org/v3/configuration/providers#options "Direct link to heading")

| Name                | Description                                                      | Type                          | Required |
| ------------------- | ---------------------------------------------------------------- | ----------------------------- | -------- |
| id                  | Unique ID for the provider                                       | `string`                      | Yes      |
| name                | Descriptive name for the provider                                | `string`                      | Yes      |
| type                | Type of provider, in this case `oauth`                           | `"oauth"`                     | Yes      |
| version             | OAuth version (e.g. '1.0', '1.0a', '2.0')                        | `string`                      | Yes      |
| scope               | OAuth access scopes (expects array or string)                    | `string` or `string[]`        | Yes      |
| params              | Extra URL params sent when calling `accessTokenUrl`              | `Object`                      | Yes      |
| accessTokenUrl      | Endpoint to retrieve an access token                             | `string`                      | Yes      |
| authorizationUrl    | Endpoint to request authorization from the user                  | `string`                      | Yes      |
| requestTokenUrl     | Endpoint to retrieve a request token                             | `string`                      | Yes      |
| profileUrl          | Endpoint to retrieve the user's profile                          | `string`                      | Yes      |
| clientId            | Client ID of the OAuth provider                                  | `string`                      | Yes      |
| clientSecret        | Client Secret of the OAuth provider                              | `string`                      | Yes      |
| profile             | A callback returning an object with the user's info              | `(profile, tokens) => Object` | Yes      |
| protection          | Additional security for OAuth login flows (defaults to `state`)  | `"pkce"`,`"state"`,`"none"`   | No       |
| state               | Same as `protection: "state"`. Being deprecated, use protection. | `boolean`                     | No       |
| headers             | Any headers that should be sent to the OAuth provider            | `Object`                      | No       |
| authorizationParams | Additional params to be sent to the authorization endpoint       | `Object`                      | No       |
| idToken             | Set to `true` for services that use ID Tokens (e.g. OpenID)      | `boolean`                     | No       |
| region              | Only when using BattleNet                                        | `string`                      | No       |
| domain              | Only when using certain Providers                                | `string`                      | No       |
| tenantId            | Only when using Azure, Active Directory, B2C, FusionAuth         | `string`                      | No       |

tip

Even if you are using a built-in provider, you can override any of these options to tweak the default configuration.

[...nextauth].js

```
    import Providers from "next-auth/providers"

    Providers.Auth0({
      clientId: process.env.CLIENT_ID,
      clientSecret: process.env.CLIENT_SECRET,
      domain: process.env.DOMAIN,
      scope: "openid your_custom_scope", // We do provide a default, but this will override it if defined
      profile(profile) {
        return {} // Return the profile in a shape that is different from the built-in one.
      },
    })

```

### Using a custom provider[​](https://next-auth.js.org/v3/configuration/providers#using-a-custom-provider "Direct link to heading")

You can use an OAuth provider that isn't built-in by using a custom object.

As an example of what this looks like, this is the provider object returned for the Google provider:

```
    {
      id: "google",
      name: "Google",
      type: "oauth",
      version: "2.0",
      scope: "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email",
      params: { grant_type: "authorization_code" },
      accessTokenUrl: "https://accounts.google.com/o/oauth2/token",
      requestTokenUrl: "https://accounts.google.com/o/oauth2/auth",
      authorizationUrl: "https://accounts.google.com/o/oauth2/auth?response_type=code",
      profileUrl: "https://www.googleapis.com/oauth2/v1/userinfo?alt=json",
      async profile(profile, tokens) {
        // You can use the tokens, in case you want to fetch more profile information
        // For example several OAuth providers do not return email by default.
        // Depending on your provider, will have tokens like `access_token`, `id_token` and or `refresh_token`
        return {
          id: profile.id,
          name: profile.name,
          email: profile.email,
          image: profile.picture
        }
      },
      clientId: "",
      clientSecret: ""
    }

```

Replace all the options in this JSON object with the ones from your custom provider - be sure to give it a unique ID and specify the correct OAuth version - and add it to the providers option when initializing the library:

pages/api/auth/[...nextauth].js

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Twitter({
        clientId: process.env.TWITTER_ID,
        clientSecret: process.env.TWITTER_SECRET,
      }),
      {
        id: 'customProvider',
        name: 'CustomProvider',
        type: 'oauth',
        version: '2.0',
        scope: ''  // Make sure to request the users email address
        ...
      }
    ]
    ...

```

### Adding a new provider[​](https://next-auth.js.org/v3/configuration/providers#adding-a-new-provider "Direct link to heading")

If you think your custom provider might be useful to others, we encourage you to open a PR and add it to the built-in list so others can discover it much more easily!

You only need to add two changes:

1. Add your config: [`src/providers/{provider}.js`](https://github.com/nextauthjs/next-auth/tree/main/packages/next-auth/src/providers)
   • make sure you use a named default export, like this: `export default function YourProvider`
2. Add provider documentation: [`www/docs/providers/{provider}.md`](https://github.com/nextauthjs/next-auth/tree/ead715219a5d7a6e882a6ba27fa56b03954d062d/www/docs/providers)
3. Add it to our [provider types](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/types/providers.d.ts) (for TS projects)
   • you just need to add your new provider name to [this list](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/types/providers.d.ts#L56-L97)
   • in case you new provider accepts some custom options, you can [add them here](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/types/providers.d.ts#L48-L53)

That's it! 🎉 Others will be able to discover this provider much more easily now!

## Email Provider[​](https://next-auth.js.org/v3/configuration/providers#email-provider "Direct link to heading")

### How to[​](https://next-auth.js.org/v3/configuration/providers#how-to-1 "Direct link to heading")

The Email provider uses email to send "magic links" that can be used sign in, you will likely have seen them before if you have used software like Slack.

Adding support for signing in via email in addition to one or more OAuth services provides a way for users to sign in if they lose access to their OAuth account (e.g. if it is locked or deleted).

Configuration is similar to other providers, but the options are different:

pages/api/auth/[...nextauth].js

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Email({
        server: process.env.EMAIL_SERVER,
        from: process.env.EMAIL_FROM,
        // maxAge: 24 * 60 * 60, // How long email links are valid for (default 24h)
      }),
    ],
    ...

```

See the [Email provider documentation](https://next-auth.js.org/providers/email) for more information on how to configure email sign in.

note

The email provider requires a database, it cannot be used without one.

### Options[​](https://next-auth.js.org/v3/configuration/providers#options-1 "Direct link to heading")

| Name                    | Description                                                                                                  | Type                             | Required |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------- | -------- |
| id                      | Unique ID for the provider                                                                                   | `string`                         | Yes      |
| name                    | Descriptive name for the provider                                                                            | `string`                         | Yes      |
| type                    | Type of provider, in this case `email`                                                                       | `"email"`                        | Yes      |
| server                  | Path or object pointing to the email server                                                                  | `string` or `Object`             | Yes      |
| sendVerificationRequest | Callback to execute when a verification request is sent                                                      | `(params) => Promise<undefined>` | Yes      |
| from                    | The email address from which emails are sent, default: "[no-reply@example.com](mailto:no-reply@example.com)" | `string`                         | No       |
| maxAge                  | How long until the e-mail can be used to log the user in seconds. Defaults to 1 day                          | `number`                         | No       |

## Credentials Provider[​](https://next-auth.js.org/v3/configuration/providers#credentials-provider "Direct link to heading")

### How to[​](https://next-auth.js.org/v3/configuration/providers#how-to-2 "Direct link to heading")

The Credentials provider allows you to handle signing in with arbitrary credentials, such as a username and password, two factor authentication or hardware device (e.g. YubiKey U2F / FIDO).

It is intended to support use cases where you have an existing system you need to authenticate users against.

pages/api/auth/[...nextauth].js

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Credentials({
        // The name to display on the sign in form (e.g. 'Sign in with...')
        name: 'Credentials',
        // The credentials is used to generate a suitable form on the sign in page.
        // You can specify whatever fields you are expecting to be submitted.
        // e.g. domain, username, password, 2FA token, etc.
        credentials: {
          username: { label: "Username", type: "text", placeholder: "jsmith" },
          password: {  label: "Password", type: "password" }
        },
        async authorize(credentials, req) {
          // You need to provide your own logic here that takes the credentials
          // submitted and returns either a object representing a user or value
          // that is false/null if the credentials are invalid.
          // e.g. return { id: 1, name: 'J Smith', email: 'jsmith@example.com' }
          // You can also use the `req` object to obtain additional parameters
          // (i.e., the request IP address)
          const res = await fetch("/your/endpoint", {
            method: 'POST',
            body: JSON.stringify(credentials),
            headers: { "Content-Type": "application/json" }
          })
          const user = await res.json()

          // If no error and we have user data, return it
          if (res.ok && user) {
            return user
          }
          // Return null if user data could not be retrieved
          return null
        }
      })
    ]
    ...

```

See the [Credentials provider documentation](https://next-auth.js.org/providers/credentials) for more information.

note

The Credentials provider can only be used if JSON Web Tokens are enabled for sessions. Users authenticated with the Credentials provider are not persisted in the database.

### Options[​](https://next-auth.js.org/v3/configuration/providers#options-2 "Direct link to heading")

| Name        | Description                                       | Type                                  | Required |
| ----------- | ------------------------------------------------- | ------------------------------------- | -------- |
| id          | Unique ID for the provider                        | `string`                              | Yes      |
| name        | Descriptive name for the provider                 | `string`                              | Yes      |
| type        | Type of provider, in this case `credentials`      | `"credentials"`                       | Yes      |
| credentials | The credentials to sign-in with                   | `Object`                              | Yes      |
| authorize   | Callback to execute once user is to be authorized | `(credentials, req) => Promise<User>` | Yes      |
