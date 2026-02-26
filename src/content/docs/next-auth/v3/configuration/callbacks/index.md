---
title: '로그인 콜백[\u200b](https://next-auth.js.org/v3/configuration/callbacks#sign-in-callback "Direct link to heading")'
description: "콜백은 작업이 수행될 때 어떤 일이 발생할지 제어하는 데 사용할 수 있는 비동기 함수입니다."
---

Source URL: https://next-auth.js.org/v3/configuration/callbacks

# 콜백 | NextAuth.js

버전: v3

콜백은 작업이 수행될 때 어떤 일이 발생할지 제어하는 데 사용할 수 있는 **비동기** 함수입니다.

콜백은 매우 강력하며, 특히 JSON Web Tokens를 사용하는 시나리오에서 데이터베이스 없이 접근 제어를 구현하고 외부 데이터베이스나 API와 통합할 수 있게 해줍니다.

tip

JSON Web Tokens를 사용할 때 Access Token 또는 User ID 같은 데이터를 브라우저로 전달하려면, `jwt` 콜백이 호출될 때 해당 데이터를 토큰에 유지한 다음 `session` 콜백에서 그 데이터를 브라우저로 전달할 수 있습니다.

아래의 각 콜백에 대해 핸들러를 지정할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    ...
      callbacks: {
        async signIn(user, account, profile) {
          return true
        },
        async redirect(url, baseUrl) {
          return baseUrl
        },
        async session(session, user) {
          return session
        },
        async jwt(token, user, account, profile, isNewUser) {
          return token
        }
    ...
    }

```

아래 문서에서는 각 콜백 구현 방법, 기본 동작, 그리고 각 콜백이 반환해야 하는 응답 예시를 보여줍니다. 사용 중인 설정 옵션과 인증 provider에 따라 콜백에 전달되는 값이 달라질 수 있습니다.

## 로그인 콜백[​](https://next-auth.js.org/v3/configuration/callbacks#sign-in-callback "Direct link to heading")

`signIn()` 콜백을 사용해 사용자의 로그인 허용 여부를 제어할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    ...
    callbacks: {
      /**
       * @param  {object} user     User object
       * @param  {object} account  Provider account
       * @param  {object} profile  Provider profile
       * @return {boolean|string}  Return `true` to allow sign in
       *                           Return `false` to deny access
       *                           Return `string` to redirect to (eg.: "/unauthorized")
       */
      async signIn(user, account, profile) {
        const isAllowedToSignIn = true
        if (isAllowedToSignIn) {
          return true
        } else {
          // Return false to display a default error message
          return false
          // Or you can return a URL to redirect to:
          // return '/unauthorized'
        }
      }
    }
    ...

```

- **Email Provider**를 사용할 때는 사용자가 **Verification Request**를 보낼 때(로그인 가능한 링크가 포함된 이메일이 발송되기 전) `signIn()` 콜백이 트리거되고, 로그인 이메일의 링크를 활성화한 _후_ 다시 한 번 트리거됩니다.

이메일 계정은 OAuth 계정처럼 프로필을 가지지 않습니다. 이메일 로그인 중 첫 번째 호출에서는 `profile` 객체에 `verificationRequest: true` 속성이 포함되어 검증 요청 흐름에서 트리거되었음을 나타냅니다. 사용자가 로그인 링크를 클릭한 _후_ 호출될 때는 이 속성이 존재하지 않습니다.

`verificationRequest` 속성을 확인하여 차단 목록에 있는 주소나 도메인으로 이메일이 발송되지 않게 하거나(또는 허용 목록의 이메일 주소에만 명시적으로 생성되게) 할 수 있습니다.

- **Credentials Provider**를 사용할 때 `user` 객체는 `authorization` 콜백이 반환한 응답이며, `profile` 객체는 `HTTP POST` 제출의 원본 body입니다.

note

데이터베이스와 함께 NextAuth.js를 사용할 때 User 객체는 사용자가 이전에 로그인한 적이 있으면 데이터베이스의 사용자 객체(User ID 포함)가 되고, 로그인한 적이 없으면 더 단순한 프로토타입 사용자 객체(예: name, email, image)가 됩니다.

데이터베이스 없이 NextAuth.js를 사용할 때 user 객체는 항상 프로필에서 추출된 정보가 담긴 프로토타입 사용자 객체입니다.

note

이 콜백이 반환한 리디렉션은 인증 흐름을 취소합니다. 예를 들어 사용자가 로그인할 수 없는 이유를 알려주는 오류 페이지로만 리디렉션하세요.

로그인 성공 후 특정 페이지로 리디렉션하려면 [the `callbackUrl` option](https://next-auth.js.org/getting-started/client#specifying-a-callbackurl) 또는 [the redirect callback](https://next-auth.js.org/configuration/callbacks#redirect-callback)을 사용하세요.

## 리디렉션 콜백[​](https://next-auth.js.org/v3/configuration/callbacks#redirect-callback "Direct link to heading")

리디렉션 콜백은 사용자가 콜백 URL로 리디렉션될 때마다(예: signin 또는 signout 시) 호출됩니다.

기본적으로 사이트와 동일한 URL의 URL만 허용되며, 이 동작은 리디렉션 콜백으로 사용자 지정할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    ...
    callbacks: {
      /**
       * @param  {string} url      URL provided as callback URL by the client
       * @param  {string} baseUrl  Default base URL of site (can be used as fallback)
       * @return {string}          URL the client will be redirect to
       */
      async redirect(url, baseUrl) {
        return url.startsWith(baseUrl)
          ? url
          : baseUrl
      }
    }
    ...

```

note

리디렉션 콜백은 같은 흐름에서 여러 번 호출될 수 있습니다.

## JWT 콜백[​](https://next-auth.js.org/v3/configuration/callbacks#jwt-callback "Direct link to heading")

이 JSON Web Token 콜백은 JSON Web Token이 생성될 때(즉, sign in 시) 또는 업데이트될 때(즉, 클라이언트에서 세션에 접근할 때마다) 호출됩니다.

예: `/api/auth/signin`, `getSession()`, `useSession()`, `/api/auth/session`

- 데이터베이스 세션 만료 시간과 마찬가지로, 세션이 활성 상태일 때마다 토큰 만료 시간도 연장됩니다.
- 인수 _user_, _account_, _profile_, _isNewUser_ 는 사용자가 로그인한 뒤 새 세션에서 이 콜백이 처음 호출될 때에만 전달됩니다.

_user_, _account_, _profile_, _isNewUser_ 의 내용은 provider 및 데이터베이스 사용 여부에 따라 달라집니다. User ID, OAuth Access Token 등의 데이터를 브라우저로 전달하려면 토큰에 유지한 뒤 `session()` 콜백에서 반환하면 됩니다.

pages/api/auth/[...nextauth].js

```
    ...
    callbacks: {
      /**
       * @param  {object}  token     Decrypted JSON Web Token
       * @param  {object}  user      User object      (only available on sign in)
       * @param  {object}  account   Provider account (only available on sign in)
       * @param  {object}  profile   Provider profile (only available on sign in)
       * @param  {boolean} isNewUser True if new user (only available on sign in)
       * @return {object}            JSON Web Token that will be saved
       */
      async jwt(token, user, account, profile, isNewUser) {
        // Add access_token to the token right after signin
        if (account?.accessToken) {
          token.accessToken = account.accessToken
        }
        return token
      }
    }
    ...

```

tip

jwt에서 token 이외의 다른 파라미터 존재 여부를 확인하는 if 분기를 사용하세요. 그중 하나라도 존재하면 jwt가 처음 호출된 것입니다. 원한다면 이 지점에서 `access_token` 같은 값을 jwt에 추가하기 좋습니다.

tip

signin 시 어떤 정보를 사용할 수 있는지 확인하려면 `token` 외의 모든 파라미터 내용도 확인하세요.

danger

NextAuth.js는 JSON Web Token에 저장할 수 있는 데이터 양을 제한하지 않지만, 브라우저는 일반적으로 쿠키당 약 **4096 byte 제한**을 적용합니다.

대량의 데이터를 유지해야 한다면 다른 곳(예: 데이터베이스)에 저장해야 합니다. 일반적인 방법은 쿠키에 키를 저장하고, 예를 들어 `session()` 콜백에서 그 키로 데이터베이스의 나머지 데이터를 조회하는 것입니다.

## 세션 콜백[​](https://next-auth.js.org/v3/configuration/callbacks#session-callback "Direct link to heading")

세션 콜백은 세션을 확인할 때마다 호출됩니다. 기본적으로 보안 강화를 위해 토큰의 일부만 반환됩니다. `jwt()` 콜백을 통해 토큰에 추가한 값을 사용 가능하게 하려면, 여기서 명시적으로 전달해 클라이언트에서 사용할 수 있게 해야 합니다.

예: `getSession()`, `useSession()`, `/api/auth/session`

- 데이터베이스 세션을 사용할 때는 User 객체가 인수로 전달됩니다.
- 세션에 JSON Web Tokens를 사용할 때는 대신 JWT payload가 제공됩니다.

pages/api/auth/[...nextauth].js

```
    ...
    callbacks: {
      /**
       * @param  {object} session      Session object
       * @param  {object} token        User object    (if using database sessions)
       *                               JSON Web Token (if not using database sessions)
       * @return {object}              Session that will be returned to the client
       */
      async session(session, token) {
        // Add property to session, like an access_token from a provider.
        session.accessToken = token.accessToken
        return session
      }
    }
    ...

```

tip

JSON Web Tokens를 사용할 때는 `session()` 콜백보다 `jwt()` 콜백이 먼저 호출되므로, JSON Web Token에 추가한 값은 provider의 `access_token` 같은 값도 포함해 세션 콜백에서 즉시 사용할 수 있습니다.

tip

값의 의미를 더 잘 나타내기 위해 JWT 세션을 사용할 때 두 번째 파라미터 이름은 `token` 으로 지정해야 합니다(`jwt()` 콜백에서 반환하는 것과 동일). 데이터베이스를 사용한다면 `user` 로 지정하세요.

danger

데이터베이스 세션을 사용하더라도 session 객체는 서버 측에 유지되지 않습니다. 세션 테이블에는 session token, user, 만료 시간 같은 데이터만 저장됩니다.

서버 측에 세션 데이터를 유지해야 한다면 세션에 대해 반환되는 `accessToken` 을 키로 사용할 수 있고, `session()` 콜백에서 데이터베이스에 연결해 해당 데이터에 접근할 수 있습니다. 세션 `accessToken` 값은 회전되지 않으며 세션이 유효한 동안 유효합니다.

데이터베이스 세션 대신 JSON Web Tokens를 사용한다면 token에 저장된 User ID 또는 고유 키를 사용해야 합니다(JSON Web Tokens를 사용할 때는 세션용 access token이 생성되지 않으므로, 로그인 시 이 키를 직접 생성해야 합니다).
