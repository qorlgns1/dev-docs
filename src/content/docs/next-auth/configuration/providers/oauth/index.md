---
title: "OAuth"
description: "NextAuth.js는 어떤 OAuth 서비스와도 동작하도록 설계되었습니다. OAuth 1.0, 1.0A, 2.0, OpenID Connect를 지원하며, 가장 널리 쓰이는 로그인 서비스 대부분을 기본 지원합니다."
---

Source URL: https://next-auth.js.org/configuration/providers/oauth

# OAuth | NextAuth.js

버전: v4

**NextAuth.js**의 인증 Provider는 사용자가 기존에 사용하던 선호 로그인으로 로그인할 수 있게 해주는 OAuth 정의입니다. 미리 정의된 다양한 Provider를 사용할 수도 있고, 직접 커스텀 OAuth 구성을 작성할 수도 있습니다.

- [내장 OAuth Provider 사용하기](https://next-auth.js.org/configuration/providers/oauth#built-in-providers) (예: Github, Twitter, Google 등)
- [커스텀 OAuth Provider 사용하기](https://next-auth.js.org/configuration/providers/oauth#using-a-custom-provider)

note

NextAuth.js는 어떤 OAuth 서비스와도 동작하도록 설계되었습니다. **OAuth 1.0**, **1.0A**, **2.0**, **OpenID Connect**를 지원하며, 가장 널리 쓰이는 로그인 서비스 대부분을 기본 지원합니다.

너무 자세한 설명은 생략하면, OAuth 흐름은 일반적으로 6단계로 구성됩니다.

1. 애플리케이션이 사용자에게 서비스 리소스 접근 권한을 요청합니다.
2. 사용자가 요청을 승인하면 애플리케이션은 authorization grant를 받습니다.
3. 애플리케이션은 자신의 신원 인증 정보와 authorization grant를 제시하여 authorization server(API)에 access token을 요청합니다.
4. 애플리케이션 신원이 인증되고 authorization grant가 유효하면, authorization server(API)가 애플리케이션에 access token을 발급합니다. 권한 부여가 완료됩니다.
5. 애플리케이션은 resource server(API)에 리소스를 요청하면서 인증을 위해 access token을 함께 제시합니다.
6. access token이 유효하면 resource server(API)가 애플리케이션에 리소스를 제공합니다.

sequenceDiagram participant Browser participant App Server participant Auth Server (Github) Note left of Browser: User clicks on "Sign in" Browser->>App Server: GET<br/>"api/auth/signin" App Server->>App Server: Computes the available<br/>sign in providers<br/>from the "providers" option App Server->>Browser: Redirects to Sign in page Note left of Browser: Sign in options<br/>are shown the user<br/>(Github, Twitter, etc...) Note left of Browser: User clicks on<br/>"Sign in with Github" Browser->>App Server: POST<br/>"api/auth/signin/github" App Server->>App Server: Computes sign in<br/>options for Github<br/>(scopes, callback URL, etc...) App Server->>Auth Server (Github): GET<br/>"github.com/login/oauth/authorize" Note left of Auth Server (Github): Sign in options<br> are supplied as<br/>query params<br/>(clientId, <br/>scope, etc...) Auth Server (Github)->>Browser: Shows sign in page<br/>in Github.com<br/>to the user Note left of Browser: User inserts their<br/>credentials in Github Browser->>Auth Server (Github): Github validates the inserted credentials Auth Server (Github)->>Auth Server (Github): Generates one time access code<br/>and calls callback<br>URL defined in<br/>App settings Auth Server (Github)->>App Server: GET<br/>"api/auth/callback/github?code=123" App Server->>App Server: Grabs code<br/>to exchange it for<br/>access token App Server->>Auth Server (Github): POST<br/>"github.com/login/oauth/access_token"<br/>{code: 123} Auth Server (Github)->>Auth Server (Github): Verifies code is<br/>valid and generates<br/>access token Auth Server (Github)->>App Server: { access_token: 16C7x... } App Server->>App Server: Generates session token<br/>and stores session App Server->>Browser: You're now logged in!

더 자세한 내용은 Aaron Parecki의 블로그 글 [OAuth2 Simplified](https://aaronparecki.com/oauth-2-simplified/) 또는 Postman의 블로그 글 [OAuth 2.0: Implicit Flow is Dead, Try PKCE Instead](https://blog.postman.com/pkce-oauth-how-to/)를 참고하세요.

## 사용 방법[​](https://next-auth.js.org/configuration/providers/oauth#how-to "Direct link to heading")

1. Provider의 개발자 포털에 애플리케이션을 등록합니다. 보통 각 지원 Provider의 문서 페이지에 등록 방법과 함께 해당 포털 링크가 포함되어 있습니다.

2. 리디렉션 URI(때로는 Callback URL이라고도 함)는 다음 형식을 따라야 합니다.

```
    [origin]/api/auth/callback/[provider]

```

`[provider]`는 Provider의 `id`를 의미합니다([options](https://next-auth.js.org/configuration/providers/oauth#options) 참고). 예를 들어 `localhost`에서 Twitter를 사용할 경우 다음과 같습니다.

```
    http://localhost:3000/api/auth/callback/twitter

```

예제 애플리케이션에서 Google을 사용하면 다음과 같습니다.

```
    https://next-auth-example.vercel.app/api/auth/callback/google

```

3. 프로젝트 루트에 `.env` 파일을 만들고 client ID와 client secret을 추가합니다. Twitter의 경우 다음과 같습니다.

```
    TWITTER_ID=YOUR_TWITTER_CLIENT_ID
    TWITTER_SECRET=YOUR_TWITTER_CLIENT_SECRET

```

4. 이제 NextAuth.js options 객체에 Provider 설정을 추가할 수 있습니다. 원하는 만큼 OAuth Provider를 추가할 수 있으며, `providers`가 배열인 것을 확인할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    import TwitterProvider from "next-auth/providers/twitter"
    ...
    providers: [
      TwitterProvider({
        clientId: process.env.TWITTER_ID,
        clientSecret: process.env.TWITTER_SECRET
      })
    ],
    ...

```

5. Provider 설정이 완료되면 다음 URL에서 로그인할 수 있습니다: `[origin]/api/auth/signin`. 설정된 모든 Provider가 표시되는 브랜딩 없는 자동 생성 페이지입니다.

![로그인 스크린샷](https://next-auth.js.org/img/signin.png)

## 옵션[​](https://next-auth.js.org/configuration/providers/oauth#options "Direct link to heading")

커스텀 OAuth Provider 또는 내장 OAuth Provider를 설정할 때 다음 옵션을 사용할 수 있습니다.

```
    interface OAuthConfig {
      /**
       * OpenID Connect (OIDC) compliant providers can configure
       * this instead of `authorize`/`token`/`userinfo` options
       * without further configuration needed in most cases.
       * You can still use the `authorize`/`token`/`userinfo`
       * options for advanced control.
       *
       * [Authorization Server Metadata](https://datatracker.ietf.org/doc/html/rfc8414#section-3)
       */
      wellKnown?: string
      /**
       * The login process will be initiated by sending the user to this URL.
       *
       * [Authorization endpoint](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1)
       */
      authorization: EndpointHandler<AuthorizationParameters>
      /**
       * Endpoint that returns OAuth 2/OIDC tokens and information about them.
       * This includes `access_token`, `id_token`, `refresh_token`, etc.
       *
       * [Token endpoint](https://datatracker.ietf.org/doc/html/rfc6749#section-3.2)
       */
      token: EndpointHandler<
        UrlParams,
        {
          /**
           * Parameters extracted from the request to the `/api/auth/callback/:providerId` endpoint.
           * Contains params like `state`.
           */
          params: CallbackParamsType
          /**
           * When using this custom flow, make sure to do all the necessary security checks.
           * This object contains parameters you have to match against the request to make sure it is valid.
           */
          checks: OAuthChecks
        },
        { tokens: TokenSet }
      >
      /**
       * When using an OAuth 2 provider, the user information must be requested
       * through an additional request from the userinfo endpoint.
       *
       * [Userinfo endpoint](https://www.oauth.com/oauth2-servers/signing-in-with-google/verifying-the-user-info)
       */
      userinfo?: EndpointHandler<UrlParams, { tokens: TokenSet }, Profile>
      type: "oauth"
      /**
       * Used in URLs to refer to a certain provider.
       * @example /api/auth/callback/twitter // where the `id` is "twitter"
       */
      id: string
      version: string
      profile(profile: P, tokens: TokenSet): Awaitable<User>
      checks?: ChecksType | ChecksType[]
      clientId: string
      clientSecret: string
      /**
       * If set to `true`, the user information will be extracted
       * from the `id_token` claims, instead of
       * making a request to the `userinfo` endpoint.
       *
       * `id_token` is usually present in OpenID Connect (OIDC) compliant providers.
       *
       * [`id_token` explanation](https://www.oauth.com/oauth2-servers/openid-connect/id-tokens)
       */
      idToken?: boolean
      region?: string
      issuer?: string
      client?: Partial<ClientMetadata>
      allowDangerousEmailAccountLinking?: boolean
      /**
       * Object containing the settings for the styling of the providers sign-in buttons
       */
      style: ProviderStyleType
    }

```

### `authorization` 옵션[​](https://next-auth.js.org/configuration/providers/oauth#authorization-option "Direct link to heading")

[_Authorization endpoint_](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1)로의 요청을 어떻게 구성할지 설정합니다.

이 옵션은 두 가지 방식으로 사용할 수 있습니다.

1. `authorization`에 `"https://example.com/oauth/authorization?scope=email"`처럼 전체 URL을 설정할 수 있습니다.
2. 다음과 같이 `url`과 `params`를 가진 객체를 사용할 수 있습니다.

```
authorization: {
           url: "https://example.com/oauth/authorization",
           params: { scope: "email" }
         }

```

tip

Provider가 OpenID Connect(OIDC)를 준수한다면 대신 `wellKnown` 옵션 사용을 권장합니다.

### `token` 옵션[​](https://next-auth.js.org/configuration/providers/oauth#token-option "Direct link to heading")

[_Token endpoint_](https://datatracker.ietf.org/doc/html/rfc6749#section-3.2)로의 요청을 어떻게 구성할지 설정합니다.

이 옵션은 세 가지 방식으로 사용할 수 있습니다.

1. `token`에 `"https://example.com/oauth/token?some=param"`처럼 전체 URL을 설정할 수 있습니다.
2. 다음과 같이 `url`과 `params`를 가진 객체를 사용할 수 있습니다.

```
token: {
           url: "https://example.com/oauth/token",
           params: { some: "param" }
         }

```

3. 요청을 완전히 직접 제어할 수 있습니다.

```
token: {
           url: "https://example.com/oauth/token",
           async request(context) {
             // context contains useful properties to help you make the request.
             const tokens = await makeTokenRequest(context)
             return { tokens }
           }
         }

```

danger

옵션 3은 대부분의 경우 필요하지 않지만, Provider가 명세를 따르지 않거나 매우 특수한 제약이 있는 경우 유용할 수 있습니다. 가능하면 피하세요.

tip

Provider가 OpenID Connect(OIDC)를 준수한다면 대신 `wellKnown` 옵션 사용을 권장합니다.

### `userinfo` 옵션[​](https://next-auth.js.org/configuration/providers/oauth#userinfo-option "Direct link to heading")

`userinfo` endpoint는 로그인된 사용자 정보를 반환합니다. OAuth 명세의 일부는 아니지만, 대부분의 Provider에서 일반적으로 제공됩니다.

이 옵션은 세 가지 방식으로 사용할 수 있습니다.

1. `userinfo`에 `"https://example.com/oauth/userinfo?some=param"`처럼 전체 URL을 설정할 수 있습니다.
2. 다음과 같이 `url`과 `params`를 가진 객체를 사용할 수 있습니다.

```
userinfo: {
           url: "https://example.com/oauth/userinfo",
           params: { some: "param" }
         }

```

3. 요청을 완전히 직접 제어할 수 있습니다.

```
userinfo: {
           url: "https://example.com/oauth/userinfo",
           // The result of this method will be the input to the `profile` callback.
           async request(context) {
             // context contains useful properties to help you make the request.
             return await makeUserinfoRequest(context)
           }
         }

```

danger

옵션 3은 대부분의 경우 필요하지 않지만, Provider가 명세를 따르지 않거나 매우 특수한 제약이 있는 경우 유용할 수 있습니다. 가능하면 피하세요.

tip

드문 경우지만 이 endpoint의 반환값이 중요하지 않거나 Provider에 해당 endpoint가 없다면 noop 함수를 만들 수 있습니다.

```
    userinfo: {
      request: () => {}
    }

```

tip

Provider가 OpenID Connect(OIDC)를 준수한다면 대신 `wellKnown` 옵션 사용을 권장합니다. OIDC는 보통 `token` endpoint에서 `id_token`을 반환합니다. `next-auth`는 추가로 `userinfo` endpoint를 호출하는 대신 `id_token`을 디코딩해 사용자 정보를 가져올 수 있습니다. Provider 설정 최상위에 `idToken: true`만 설정하면 됩니다. 설정하지 않으면 `next-auth`는 여전히 이 endpoint에 접속을 시도합니다.

### `client` 옵션[​](https://next-auth.js.org/configuration/providers/oauth#client-option "Direct link to heading")

고급 옵션이며, 대부분의 경우 필요하지 않기를 바랍니다. `next-auth`는 내부적으로 `openid-client`를 사용합니다. 이 옵션 관련 문서는 [여기](https://github.com/panva/node-openid-client/blob/main/docs/README.md#new-clientmetadata-jwks-options)에서 확인하세요.

### `allowDangerousEmailAccountLinking` 옵션[​](https://next-auth.js.org/configuration/providers/oauth#allowdangerousemailaccountlinking-option "Direct link to heading")

일반적으로 OAuth Provider로 로그인할 때 같은 이메일 주소를 가진 다른 계정이 이미 존재하더라도 계정은 자동으로 연결되지 않습니다. 로그인 시 임의 Provider 간 자동 계정 연결은 안전하지 않기 때문에 기본적으로 비활성화되어 있습니다([Security FAQ](https://next-auth.js.org/faq#security) 참고). 하지만 해당 Provider가 계정에 연결된 이메일 주소를 안전하게 검증한다고 신뢰할 수 있다면 자동 계정 연결을 허용하는 것이 바람직할 수 있습니다. 자동 계정 연결을 활성화하려면 Provider 설정에 `allowDangerousEmailAccountLinking: true`를 설정하세요.

사용자가 이미 어떤 Provider로든 로그인된 상태에서 다른 Provider로 다시 `signIn`을 사용하면, 새 Provider 계정은 같은 인증 사용자에게 자동으로 연결됩니다. 이 동작은 각 Provider 계정의 기본 이메일과 무관하게 발생합니다. 이 흐름은 `allowDangerousEmailAccountLinking` 옵션의 영향을 받지 않습니다.

## 커스텀 provider 사용하기[​](https://next-auth.js.org/configuration/providers/oauth#using-a-custom-provider "Direct link to heading")

커스텀 객체를 사용해 내장되지 않은 OAuth Provider를 사용할 수 있습니다.

예시로, Google Provider에서 반환되는 provider 객체는 다음과 같습니다.

```
    {
      id: "google",
      name: "Google",
      type: "oauth",
      wellKnown: "https://accounts.google.com/.well-known/openid-configuration",
      authorization: { params: { scope: "openid email profile" } },
      idToken: true,
      checks: ["pkce", "state"],
      profile(profile) {
        return {
          id: profile.sub,
          name: profile.name,
          email: profile.email,
          image: profile.picture,
        }
      },
    }

```

보시다시피 Provider가 OpenID Connect를 지원하고 `/.well-known/openid-configuration` endpoint에 `grant_type`: `authorization_code` 지원이 포함되어 있다면, 해당 설정 파일 URL을 전달하고 `name`, `type` 같은 기본 필드만 정의하면 됩니다.

그렇지 않다면 OAuth2.0 흐름의 각 단계에 대해 더 완전한 URL 세트를 전달할 수 있습니다. 예:

```
    {
      id: "kakao",
      name: "Kakao",
      type: "oauth",
      authorization: "https://kauth.kakao.com/oauth/authorize",
      token: "https://kauth.kakao.com/oauth/token",
      userinfo: "https://kapi.kakao.com/v2/user/me",
      profile(profile) {
        return {
          id: profile.id,
          name: profile.kakao_account?.profile.nickname,
          email: profile.kakao_account?.email,
          image: profile.kakao_account?.profile.profile_image_url,
        }
      },
    }

```

이 JSON 객체의 모든 옵션을 커스텀 Provider의 값으로 교체하세요. 고유한 ID를 지정하고 필요한 URL을 명시한 뒤, 라이브러리 초기화 시 providers 배열에 추가하면 됩니다.

pages/api/auth/[...nextauth].js

```
    import TwitterProvider from "next-auth/providers/twitter"
    ...
    providers: [
      TwitterProvider({
        clientId: process.env.TWITTER_ID,
        clientSecret: process.env.TWITTER_SECRET,
      }),
      {
        id: 'customProvider',
        name: 'CustomProvider',
        type: 'oauth',
        scope: ''  // Make sure to request the users email address
        ...
      }
    ]
    ...

```

## 내장 provider[​](https://next-auth.js.org/configuration/providers/oauth#built-in-providers "Direct link to heading")

NextAuth.js에는 내장 provider 세트가 포함되어 있습니다. [여기](https://github.com/nextauthjs/next-auth/tree/v4/packages/next-auth/src/providers)에서 확인할 수 있습니다. 각 내장 provider에는 전용 문서 페이지가 있습니다:

[42 School](https://next-auth.js.org/providers/42-school),[Amazon Cognito](https://next-auth.js.org/providers/cognito),[Apple](https://next-auth.js.org/providers/apple),[Atlassian](https://next-auth.js.org/providers/atlassian),[Auth0](https://next-auth.js.org/providers/auth0),[Authentik](https://next-auth.js.org/providers/authentik),[Azure Active Directory](https://next-auth.js.org/providers/azure-ad),[Azure Active Directory B2C](https://next-auth.js.org/providers/azure-ad-b2c),[Battle.net](https://next-auth.js.org/providers/battle.net),[Box](https://next-auth.js.org/providers/box),[BoxyHQ SAML](https://next-auth.js.org/providers/boxyhq-saml),[Bungie](https://next-auth.js.org/providers/bungie),[Coinbase](https://next-auth.js.org/providers/coinbase),[Discord](https://next-auth.js.org/providers/discord),[Dropbox](https://next-auth.js.org/providers/dropbox),[DuendeIdentityServer6](https://next-auth.js.org/providers/duende-identityserver6),[EVE Online](https://next-auth.js.org/providers/eveonline),[Facebook](https://next-auth.js.org/providers/facebook),[FACEIT](https://next-auth.js.org/providers/faceit),[Foursquare](https://next-auth.js.org/providers/foursquare),[Freshbooks](https://next-auth.js.org/providers/freshbooks),[FusionAuth](https://next-auth.js.org/providers/fusionauth),[GitHub](https://next-auth.js.org/providers/github),[GitLab](https://next-auth.js.org/providers/gitlab),[Google](https://next-auth.js.org/providers/google),[HubSpot](https://next-auth.js.org/providers/hubspot),[IdentityServer4](https://next-auth.js.org/providers/identity-server4),[Instagram](https://next-auth.js.org/providers/instagram),[Kakao](https://next-auth.js.org/providers/kakao),[Keycloak](https://next-auth.js.org/providers/keycloak),[LINE](https://next-auth.js.org/providers/line),[LinkedIn](https://next-auth.js.org/providers/linkedin),[Mail.ru](https://next-auth.js.org/providers/mailru),[Mailchimp](https://next-auth.js.org/providers/mailchimp),[Medium](https://next-auth.js.org/providers/medium),[Naver](https://next-auth.js.org/providers/naver),[Netlify](https://next-auth.js.org/providers/netlify),[Okta](https://next-auth.js.org/providers/okta),[OneLogin](https://next-auth.js.org/providers/onelogin),[Osso](https://next-auth.js.org/providers/osso),[osu!](https://next-auth.js.org/providers/osu),[Patreon](https://next-auth.js.org/providers/patreon),[Pinterest](https://next-auth.js.org/providers/pinterest),[Pipedrive](https://next-auth.js.org/providers/pipedrive),[Reddit](https://next-auth.js.org/providers/reddit),[Salesforce](https://next-auth.js.org/providers/salesforce),[Slack](https://next-auth.js.org/providers/slack),[Spotify](https://next-auth.js.org/providers/spotify),[Strava](https://next-auth.js.org/providers/strava),[Todoist](https://next-auth.js.org/providers/todoist),[Trakt](https://next-auth.js.org/providers/trakt),[Twitch](https://next-auth.js.org/providers/twitch),[Twitter](https://next-auth.js.org/providers/twitter),[United Effects](https://next-auth.js.org/providers/united-effects),[VK](https://next-auth.js.org/providers/vk),[Wikimedia](https://next-auth.js.org/providers/wikimedia),[WordPress.com](https://next-auth.js.org/providers/wordpress),[WorkOS](https://next-auth.js.org/providers/workos),[Yandex](https://next-auth.js.org/providers/yandex),[Zitadel](https://next-auth.js.org/providers/zitadel),[Zoho](https://next-auth.js.org/providers/zoho),[Zoom](https://next-auth.js.org/providers/zoom),

### 기본 옵션 재정의[​](https://next-auth.js.org/configuration/providers/oauth#override-default-options "Direct link to heading")

내장 프로바이더의 경우, 대부분 `clientId`와 `clientSecret`만 지정하면 됩니다. 기본값을 재정의해야 한다면, 사용자 정의 [options](https://next-auth.js.org/configuration/providers/oauth#options)를 추가하세요.

내장 프로바이더를 사용하더라도, 기본 구성을 조정하기 위해 이러한 옵션을 원하는 대로 재정의할 수 있습니다.

note

사용자가 제공한 옵션은 기본 옵션과 깊은 병합(deep merge)됩니다. 즉, 다르게 설정이 필요한 옵션의 일부만 재정의하면 됩니다. 예를 들어 scope를 다르게 하고 싶다면 `authorization.params.scope`만 재정의하면 충분하며, 전체 `authorization` 옵션을 재정의할 필요는 없습니다.

/api/auth/[...nextauth].js

```
    import Auth0Provider from "next-auth/providers/auth0"

    Auth0Provider({
      clientId: process.env.CLIENT_ID,
      clientSecret: process.env.CLIENT_SECRET,
      issuer: process.env.ISSUER,
      authorization: { params: { scope: "openid your_custom_scope" } },
    })

```

또 다른 예로, `profile` 콜백은 기본적으로 `id`, `name`, `email`, `picture`를 반환하지만, 프로바이더에서 더 많은 정보가 필요할 수 있습니다. 올바른 scope를 설정한 뒤에는 다음과 같이 처리할 수 있습니다:

/api/auth/[...nextauth].js

```
    import GoogleProvider from "next-auth/providers/google"

    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
      profile(profile) {
        return {
          // Return all the profile information you need.
          // The only truly required field is `id`
          // to be able identify the account when added to a database
        }
      },
    })

```

자동 계정 연결을 활성화하는 방법의 예시:

/api/auth/[...nextauth].js

```
    import GoogleProvider from "next-auth/providers/google"

    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
      allowDangerousEmailAccountLinking: true,
    })

```
