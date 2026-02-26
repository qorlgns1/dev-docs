---
title: "Callbacks"
description: "Callbacks는 작업이 수행될 때 어떤 일이 일어나는지 제어할 수 있는 비동기 함수입니다."
---

Source URL: https://next-auth.js.org/configuration/callbacks

# Callbacks | NextAuth.js

Version: v4

Callbacks는 작업이 수행될 때 어떤 일이 일어나는지 제어할 수 있는 **비동기** 함수입니다.

Callbacks는 매우 강력하며, 특히 JSON Web Token을 사용하는 시나리오에서 유용합니다. 데이터베이스 없이 접근 제어를 구현하고 외부 데이터베이스나 API와 통합할 수 있게 해주기 때문입니다.

tip

JSON Web Token을 사용할 때 Access Token이나 User ID 같은 데이터를 브라우저로 전달하려면, `jwt` callback이 호출될 때 해당 데이터를 토큰에 저장한 뒤 `session` callback에서 그 데이터를 브라우저로 전달할 수 있습니다.

아래의 각 callback에 대해 핸들러를 지정할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    ...
      callbacks: {
        async signIn({ user, account, profile, email, credentials }) {
          return true
        },
        async redirect({ url, baseUrl }) {
          return baseUrl
        },
        async session({ session, user, token }) {
          return session
        },
        async jwt({ token, user, account, profile, isNewUser }) {
          return token
        }
    ...
    }

```

아래 문서에서는 각 callback의 구현 방법, 기본 동작, 그리고 각 callback이 반환해야 하는 응답 예시를 보여줍니다. 사용 중인 설정 옵션과 인증 provider에 따라 callback으로 전달되는 값이 달라질 수 있습니다.

## Sign in callback[​](https://next-auth.js.org/configuration/callbacks#sign-in-callback "헤딩으로 직접 이동 링크")

사용자의 로그인 허용 여부를 제어하려면 `signIn()` callback을 사용하세요.

pages/api/auth/[...nextauth].js

```
    ...
    callbacks: {
      async signIn({ user, account, profile, email, credentials }) {
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

- **Email Provider**를 사용할 때 `signIn()` callback은 사용자가 **Verification Request**를 보낼 때(로그인 가능한 링크가 포함된 이메일이 전송되기 전) 한 번 호출되고, 이후 로그인 이메일의 링크를 활성화한 뒤 다시 한 번 호출됩니다.

이메일 계정은 OAuth 계정과 같은 방식의 프로필을 가지지 않습니다. 이메일 로그인 중 첫 번째 호출에서는 `email` 객체에 `verificationRequest: true` 속성이 포함되어, 검증 요청 흐름에서 호출되었음을 나타냅니다. 사용자가 로그인 링크를 클릭한 _이후_ 에 callback이 호출되면 이 속성은 존재하지 않습니다.

`verificationRequest` 속성을 확인해 차단 목록(blocklist)에 있는 주소나 도메인으로 이메일이 전송되지 않도록 하거나, 허용 목록(allow list)에 있는 이메일 주소에만 명시적으로 생성되도록 할 수 있습니다.

- **Credentials Provider**를 사용할 때 `user` 객체는 `authorize` callback의 반환값이며, `profile` 객체는 `HTTP POST` 제출의 원본 본문(raw body)입니다.

note

데이터베이스와 함께 NextAuth.js를 사용할 때 User 객체는, 사용자가 이전에 로그인한 적이 있으면 데이터베이스의 사용자 객체(User ID 포함)가 되고, 로그인한 적이 없으면 더 단순한 프로토타입 사용자 객체(예: name, email, image)가 됩니다.

데이터베이스 없이 NextAuth.js를 사용할 때 user 객체는 항상 프로필에서 추출된 정보를 가진 프로토타입 사용자 객체입니다.

note

이 callback이 반환한 리디렉션은 인증 흐름을 취소합니다. 예를 들어 사용자가 로그인할 수 없는 이유를 안내하는 오류 페이지로만 리디렉션하세요.

성공적인 로그인 후 페이지로 리디렉션하려면 [the `callbackUrl` option](https://next-auth.js.org/getting-started/client#specifying-a-callbackurl) 또는 [the redirect callback](https://next-auth.js.org/configuration/callbacks#redirect-callback)을 사용하세요.

## Redirect callback[​](https://next-auth.js.org/configuration/callbacks#redirect-callback "헤딩으로 직접 이동 링크")

redirect callback은 사용자가 callback URL(예: signin 또는 signout 시)로 리디렉션될 때마다 호출됩니다.

기본적으로 사이트와 동일한 URL의 주소만 허용되며, redirect callback을 사용해 이 동작을 커스터마이즈할 수 있습니다.

기본 redirect callback은 다음과 같습니다.

pages/api/auth/[...nextauth].js

```
    ...
    callbacks: {
      async redirect({ url, baseUrl }) {
        // Allows relative callback URLs
        if (url.startsWith("/")) return `${baseUrl}${url}`
        // Allows callback URLs on the same origin
        else if (new URL(url).origin === baseUrl) return url
        return baseUrl
      }
    }
    ...

```

note

동일한 흐름에서 redirect callback이 여러 번 호출될 수 있습니다.

## JWT callback[​](https://next-auth.js.org/configuration/callbacks#jwt-callback "헤딩으로 직접 이동 링크")

이 callback은 JSON Web Token이 생성될 때(즉, 로그인 시) 또는 업데이트될 때(즉, 클라이언트에서 세션에 접근할 때마다) 호출됩니다. 반환값은 [encrypted](https://next-auth.js.org/configuration/options#jwt)되며 쿠키에 저장됩니다.

`/api/auth/signin`, `/api/auth/session` 요청과 `getSession()`, `getServerSession()`, `useSession()` 호출은 이 함수를 호출합니다. 단, [JWT session](https://next-auth.js.org/configuration/options#session)을 사용하는 경우에만 해당합니다. 세션을 데이터베이스에 저장하는 경우에는 이 메서드가 호출되지 않습니다.

- 데이터베이스에 저장된 세션 만료 시간과 마찬가지로, 세션이 활성 상태인 동안 토큰 만료 시간도 연장됩니다.
- _user_, _account_, _profile_, _isNewUser_ 인자는 사용자가 로그인해 새 세션에서 이 callback이 처음 호출될 때만 전달됩니다. 이후 호출에서는 `token`만 사용할 수 있습니다.

_user_, _account_, _profile_, *isNewUser*의 내용은 provider와 데이터베이스 사용 여부에 따라 달라집니다. 이 토큰에 User ID, OAuth Access Token 같은 데이터를 저장할 수 있습니다. 아래 예시에서 `access_token`과 `user.id`를 확인하세요. 이를 클라이언트 측에 노출하려면 [`session()` callback](https://next-auth.js.org/configuration/callbacks#session-callback)도 함께 확인하세요.

pages/api/auth/[...nextauth].js

```
    ...
    callbacks: {
      async jwt({ token, account, profile }) {
        // Persist the OAuth access_token and or the user id to the token right after signin
        if (account) {
          token.accessToken = account.access_token
          token.id = profile.id
        }
        return token
      }
    }
    ...

```

tip

(`token`을 제외한) 파라미터 존재 여부를 `if` 분기로 확인하세요. 값이 존재하면 callback이 처음 호출된 것(즉, 사용자가 로그인 중)임을 의미합니다. 이 시점은 JWT에 `access_token` 같은 추가 데이터를 저장하기에 적절합니다. 이후 호출에는 `token` 파라미터만 포함됩니다.

## Session callback[​](https://next-auth.js.org/configuration/callbacks#session-callback "헤딩으로 직접 이동 링크")

session callback은 세션을 확인할 때마다 호출됩니다. 기본적으로 **보안 강화를 위해 토큰의 일부만 반환됩니다**. `jwt()` callback을 통해 토큰에 추가한 값(위의 `access_token`, `user.id` 등)을 사용 가능하게 하려면, 클라이언트에서 사용할 수 있도록 여기에서 명시적으로 전달해야 합니다.

예: `getSession()`, `useSession()`, `/api/auth/session`

- 데이터베이스 세션을 사용할 때는 User(`user`) 객체가 인자로 전달됩니다.
- 세션에 JSON Web Token을 사용할 때는 JWT payload(`token`)가 대신 제공됩니다.

pages/api/auth/[...nextauth].js

```
    ...
    callbacks: {
      async session({ session, token, user }) {
        // Send properties to the client, like an access_token and user id from a provider.
        session.accessToken = token.accessToken
        session.user.id = token.id

        return session
      }
    }
    ...

```

tip

JSON Web Token을 사용할 때는 `session()` callback보다 `jwt()` callback이 먼저 호출됩니다. 따라서 JSON Web Token에 추가한 값은(예: provider의 `access_token` 또는 `id`) 즉시 session callback에서 사용할 수 있습니다.

danger

session 객체는 데이터베이스 세션을 사용할 때도 서버 측에 저장되지 않습니다. 세션 테이블에는 세션 토큰, 사용자, 만료 시간 같은 데이터만 저장됩니다.

세션 데이터를 서버 측에 저장해야 한다면, 세션에 대해 반환되는 `accessToken`을 키로 사용할 수 있습니다. 그리고 `session()` callback에서 데이터베이스에 연결해 해당 데이터를 조회하세요. 세션 `accessToken` 값은 순환(rotating)되지 않으며, 세션이 유효한 동안 계속 유효합니다.

데이터베이스 세션 대신 JSON Web Token을 사용하는 경우, 토큰에 저장된 User ID나 고유 키를 사용해야 합니다(이 경우 세션용 access token은 생성되지 않으므로 로그인 시 직접 키를 생성해야 합니다).
