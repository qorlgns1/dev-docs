---
title: "프로바이더"
description: "사용자가 로그인할 수 있는 방법은 네 가지입니다:"
---

소스 URL: https://next-auth.js.org/v3/configuration/providers

# 프로바이더 | NextAuth.js

버전: v3

**NextAuth.js**의 인증 프로바이더는 사용자를 로그인시키는 데 사용할 수 있는 서비스입니다.

사용자가 로그인할 수 있는 방법은 네 가지입니다:

- [내장 OAuth 프로바이더 사용](https://next-auth.js.org/v3/configuration/providers#oauth-providers) (예: Github, Twitter, Google 등...)
- [커스텀 OAuth 프로바이더 사용](https://next-auth.js.org/v3/configuration/providers#using-a-custom-provider)
- [Email 사용](https://next-auth.js.org/v3/configuration/providers#email-provider)
- [Credentials 사용](https://next-auth.js.org/v3/configuration/providers#credentials-provider)

note

NextAuth.js는 어떤 OAuth 서비스와도 동작하도록 설계되었으며, **OAuth 1.0**, **1.0A**, **2.0**을 지원하고 대부분의 인기 로그인 서비스에 대한 내장 지원을 제공합니다.

## OAuth 프로바이더[​](https://next-auth.js.org/v3/configuration/providers#oauth-providers "Direct link to heading")

### 사용 가능한 프로바이더[​](https://next-auth.js.org/v3/configuration/providers#available-providers "Direct link to heading")

[42 School](https://next-auth.js.org/providers/42-school),[Amazon Cognito](https://next-auth.js.org/providers/cognito),[Apple](https://next-auth.js.org/providers/apple),[Atlassian](https://next-auth.js.org/providers/atlassian),[Auth0](https://next-auth.js.org/providers/auth0),[Authentik](https://next-auth.js.org/providers/authentik),[Azure Active Directory](https://next-auth.js.org/providers/azure-ad),[Azure Active Directory B2C](https://next-auth.js.org/providers/azure-ad-b2c),[Battle.net](https://next-auth.js.org/providers/battle.net),[Box](https://next-auth.js.org/providers/box),[BoxyHQ SAML](https://next-auth.js.org/providers/boxyhq-saml),[Bungie](https://next-auth.js.org/providers/bungie),[Coinbase](https://next-auth.js.org/providers/coinbase),[Discord](https://next-auth.js.org/providers/discord),[Dropbox](https://next-auth.js.org/providers/dropbox),[DuendeIdentityServer6](https://next-auth.js.org/providers/duende-identityserver6),[EVE Online](https://next-auth.js.org/providers/eveonline),[Facebook](https://next-auth.js.org/providers/facebook),[FACEIT](https://next-auth.js.org/providers/faceit),[Foursquare](https://next-auth.js.org/providers/foursquare),[Freshbooks](https://next-auth.js.org/providers/freshbooks),[FusionAuth](https://next-auth.js.org/providers/fusionauth),[GitHub](https://next-auth.js.org/providers/github),[GitLab](https://next-auth.js.org/providers/gitlab),[Google](https://next-auth.js.org/providers/google),[HubSpot](https://next-auth.js.org/providers/hubspot),[IdentityServer4](https://next-auth.js.org/providers/identity-server4),[Instagram](https://next-auth.js.org/providers/instagram),[Kakao](https://next-auth.js.org/providers/kakao),[Keycloak](https://next-auth.js.org/providers/keycloak),[LINE](https://next-auth.js.org/providers/line),[LinkedIn](https://next-auth.js.org/providers/linkedin),[Mail.ru](https://next-auth.js.org/providers/mailru),[Mailchimp](https://next-auth.js.org/providers/mailchimp),[Medium](https://next-auth.js.org/providers/medium),[Naver](https://next-auth.js.org/providers/naver),[Netlify](https://next-auth.js.org/providers/netlify),[Okta](https://next-auth.js.org/providers/okta),[OneLogin](https://next-auth.js.org/providers/onelogin),[Osso](https://next-auth.js.org/providers/osso),[osu!](https://next-auth.js.org/providers/osu),[Patreon](https://next-auth.js.org/providers/patreon),[Pinterest](https://next-auth.js.org/providers/pinterest),[Pipedrive](https://next-auth.js.org/providers/pipedrive),[Reddit](https://next-auth.js.org/providers/reddit),[Salesforce](https://next-auth.js.org/providers/salesforce),[Slack](https://next-auth.js.org/providers/slack),[Spotify](https://next-auth.js.org/providers/spotify),[Strava](https://next-auth.js.org/providers/strava),[Todoist](https://next-auth.js.org/providers/todoist),[Trakt](https://next-auth.js.org/providers/trakt),[Twitch](https://next-auth.js.org/providers/twitch),[Twitter](https://next-auth.js.org/providers/twitter),[United Effects](https://next-auth.js.org/providers/united-effects),[VK](https://next-auth.js.org/providers/vk),[Wikimedia](https://next-auth.js.org/providers/wikimedia),[WordPress.com](https://next-auth.js.org/providers/wordpress),[WorkOS](https://next-auth.js.org/providers/workos),[Yandex](https://next-auth.js.org/providers/yandex),[Zitadel](https://next-auth.js.org/providers/zitadel),[Zoho](https://next-auth.js.org/providers/zoho),[Zoom](https://next-auth.js.org/providers/zoom),

### 방법[​](https://next-auth.js.org/v3/configuration/providers#how-to "Direct link to heading")

1. 프로바이더의 개발자 포털에서 애플리케이션을 등록하세요. 위에는 지원되는 대부분의 프로바이더에 대해 애플리케이션 등록 방법이 자세히 나와 있는 개발자 문서 링크가 있습니다.

2. 리디렉션 URI는 다음 형식을 따라야 합니다:

```
    [origin]/api/auth/callback/[provider]

```

예를 들어 `localhost`에서 Twitter의 경우 다음과 같습니다:

```
    http://localhost:3000/api/auth/callback/twitter

```

3. 프로젝트 루트에 `.env` 파일을 만들고 client ID와 client secret을 추가하세요. Twitter의 경우 다음과 같습니다:

```
    TWITTER_ID=YOUR_TWITTER_CLIENT_ID
    TWITTER_SECRET=YOUR_TWITTER_CLIENT_SECRET

```

4. 이제 NextAuth.js options object에 프로바이더 설정을 추가할 수 있습니다. 보시다시피 `providers`는 배열입니다.

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

5. 프로바이더 설정이 완료되면 다음 URL에서 로그인할 수 있습니다: `[origin]/api/auth/signin`. 이는 구성된 모든 프로바이더가 표시되는 브랜딩 없는 자동 생성 페이지입니다.

### 옵션[​](https://next-auth.js.org/v3/configuration/providers#options "Direct link to heading")

| 이름                | 설명                                                                 | 타입                          | 필수   |
| ------------------- | -------------------------------------------------------------------- | ----------------------------- | ------ |
| id                  | 프로바이더의 고유 ID                                                 | `string`                      | 예     |
| name                | 프로바이더를 설명하는 이름                                           | `string`                      | 예     |
| type                | 프로바이더 타입, 이 경우 `oauth`                                     | `"oauth"`                     | 예     |
| version             | OAuth 버전 (예: '1.0', '1.0a', '2.0')                                | `string`                      | 예     |
| scope               | OAuth 접근 스코프 (배열 또는 문자열 기대)                            | `string` or `string[]`        | 예     |
| params              | `accessTokenUrl` 호출 시 전송되는 추가 URL params                    | `Object`                      | 예     |
| accessTokenUrl      | 액세스 토큰을 가져오는 endpoint                                      | `string`                      | 예     |
| authorizationUrl    | 사용자에게 권한을 요청하는 endpoint                                  | `string`                      | 예     |
| requestTokenUrl     | 요청 토큰을 가져오는 endpoint                                        | `string`                      | 예     |
| profileUrl          | 사용자 프로필을 가져오는 endpoint                                    | `string`                      | 예     |
| clientId            | OAuth 프로바이더의 Client ID                                         | `string`                      | 예     |
| clientSecret        | OAuth 프로바이더의 Client Secret                                     | `string`                      | 예     |
| profile             | 사용자 정보 객체를 반환하는 콜백                                     | `(profile, tokens) => Object` | 예     |
| protection          | OAuth 로그인 플로우를 위한 추가 보안 (`state`가 기본값)              | `"pkce"`,`"state"`,`"none"`   | 아니요 |
| state               | `protection: "state"`와 동일. deprecated 예정이므로 protection 사용. | `boolean`                     | 아니요 |
| headers             | OAuth 프로바이더로 전송해야 하는 헤더                                | `Object`                      | 아니요 |
| authorizationParams | authorization endpoint로 전송할 추가 params                          | `Object`                      | 아니요 |
| idToken             | ID Token을 사용하는 서비스(예: OpenID)에는 `true`로 설정             | `boolean`                     | 아니요 |
| region              | BattleNet 사용 시에만                                                | `string`                      | 아니요 |
| domain              | 특정 프로바이더 사용 시에만                                          | `string`                      | 아니요 |
| tenantId            | Azure, Active Directory, B2C, FusionAuth 사용 시에만                 | `string`                      | 아니요 |

tip

내장 프로바이더를 사용하더라도, 기본 구성을 조정하기 위해 이 옵션들을 원하는 대로 override할 수 있습니다.

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

### 커스텀 프로바이더 사용[​](https://next-auth.js.org/v3/configuration/providers#using-a-custom-provider "Direct link to heading")

커스텀 object를 사용하면 내장되지 않은 OAuth 프로바이더도 사용할 수 있습니다.

예시로, 아래는 Google 프로바이더가 반환하는 provider object입니다:

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

이 JSON object의 모든 옵션을 커스텀 프로바이더의 값으로 교체하세요. 고유 ID를 지정하고 올바른 OAuth 버전을 명시해야 합니다. 그런 다음 라이브러리를 초기화할 때 providers 옵션에 추가하세요:

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

### 새 프로바이더 추가[​](https://next-auth.js.org/v3/configuration/providers#adding-a-new-provider "Direct link to heading")

커스텀 프로바이더가 다른 사람들에게도 유용할 것 같다면, PR을 열어 내장 목록에 추가해 주세요. 그러면 다른 사람들이 훨씬 쉽게 찾을 수 있습니다!

다음 세 가지 변경만 추가하면 됩니다:

1. 설정 추가: [`src/providers/{provider}.js`](https://github.com/nextauthjs/next-auth/tree/main/packages/next-auth/src/providers)
   • `export default function YourProvider`처럼 named default export를 사용해야 합니다.
2. 프로바이더 문서 추가: [`www/docs/providers/{provider}.md`](https://github.com/nextauthjs/next-auth/tree/ead715219a5d7a6e882a6ba27fa56b03954d062d/www/docs/providers)
3. [provider types](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/types/providers.d.ts)에도 추가 (TS 프로젝트용)
   • [이 목록](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/types/providers.d.ts#L56-L97)에 새 프로바이더 이름만 추가하면 됩니다.
   • 새 프로바이더가 커스텀 옵션을 받는 경우 [여기에 추가](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/types/providers.d.ts#L48-L53)할 수 있습니다.

끝입니다! 🎉 이제 다른 사람들이 이 프로바이더를 훨씬 더 쉽게 찾을 수 있습니다!

## Email 프로바이더[​](https://next-auth.js.org/v3/configuration/providers#email-provider "Direct link to heading")

### 방법[​](https://next-auth.js.org/v3/configuration/providers#how-to-1 "Direct link to heading")

Email 프로바이더는 이메일로 로그인에 사용할 수 있는 "magic links"를 보냅니다. Slack 같은 소프트웨어를 사용해 봤다면 이미 본 적이 있을 가능성이 높습니다.

하나 이상의 OAuth 서비스에 더해 이메일 로그인 지원을 추가하면, 사용자가 OAuth 계정에 접근할 수 없게 되었을 때(예: 잠기거나 삭제된 경우) 로그인할 수 있는 방법을 제공합니다.

구성 방식은 다른 프로바이더와 비슷하지만 옵션은 다릅니다:

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

이메일 로그인 구성에 대한 자세한 내용은 [Email provider documentation](https://next-auth.js.org/providers/email)을 참고하세요.

note

email 프로바이더는 데이터베이스가 필요하며, 데이터베이스 없이 사용할 수 없습니다.

### 옵션[​](https://next-auth.js.org/v3/configuration/providers#options-1 "Direct link to heading")

| 이름                    | 설명                                                                            | 타입                             | 필수   |
| ----------------------- | ------------------------------------------------------------------------------- | -------------------------------- | ------ |
| id                      | 프로바이더의 고유 ID                                                            | `string`                         | 예     |
| name                    | 프로바이더를 설명하는 이름                                                      | `string`                         | 예     |
| type                    | 프로바이더 타입, 이 경우 `email`                                                | `"email"`                        | 예     |
| server                  | 이메일 서버를 가리키는 경로 또는 object                                         | `string` or `Object`             | 예     |
| sendVerificationRequest | verification 요청 전송 시 실행할 콜백                                           | `(params) => Promise<undefined>` | 예     |
| from                    | 이메일 발신 주소, 기본값: "[no-reply@example.com](mailto:no-reply@example.com)" | `string`                         | 아니요 |
| maxAge                  | 사용자를 로그인시키는 데 이메일을 사용할 수 있는 시간(초). 기본값은 1일         | `number`                         | 아니요 |

## Credentials 프로바이더[​](https://next-auth.js.org/v3/configuration/providers#credentials-provider "Direct link to heading")

### 방법[​](https://next-auth.js.org/v3/configuration/providers#how-to-2 "Direct link to heading")

Credentials 프로바이더를 사용하면 사용자 이름/비밀번호, 이중 인증, 하드웨어 장치(예: YubiKey U2F / FIDO) 같은 임의의 자격 증명으로 로그인 처리를 할 수 있습니다.

기존 사용자 인증 시스템에 연동해야 하는 사용 사례를 지원하기 위한 용도입니다.

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

자세한 내용은 [Credentials provider documentation](https://next-auth.js.org/providers/credentials)을 참고하세요.

note

Credentials 프로바이더는 세션에 JSON Web Tokens가 활성화된 경우에만 사용할 수 있습니다. Credentials 프로바이더로 인증된 사용자는 데이터베이스에 영속 저장되지 않습니다.

### 옵션[​](https://next-auth.js.org/v3/configuration/providers#options-2 "Direct link to heading")

| 이름        | 설명                               | 타입                                  | 필수 여부 |
| ----------- | ---------------------------------- | ------------------------------------- | --------- |
| id          | 공급자의 고유 ID                   | `string`                              | 예        |
| name        | 공급자를 설명하는 이름             | `string`                              | 예        |
| type        | 공급자 유형, 이 경우 `credentials` | `"credentials"`                       | 예        |
| credentials | 로그인에 사용할 자격 증명          | `Object`                              | 예        |
| authorize   | 사용자가 인증될 때 실행할 콜백     | `(credentials, req) => Promise<User>` | 예        |
