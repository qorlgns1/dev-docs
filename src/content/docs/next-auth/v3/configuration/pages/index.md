---
title: "Pages"
description: "NextAuth.js는 Sign in, Sign out, Email Verification을 처리하고 오류 메시지를 표시하기 위한 단순한 비브랜딩 인증 페이지를 자동으로 생성합니다."
---

Source URL: https://next-auth.js.org/v3/configuration/pages

# Pages | NextAuth.js

Version: v3

NextAuth.js는 Sign in, Sign out, Email Verification을 처리하고 오류 메시지를 표시하기 위한 단순한 비브랜딩 인증 페이지를 자동으로 생성합니다.

회원가입 페이지에 표시되는 옵션은 NextAuth.js에 전달된 옵션에서 지정한 provider를 기반으로 자동 생성됩니다.

커스텀 로그인 페이지를 추가하려면 `pages` 옵션을 사용할 수 있습니다:

pages/api/auth/[...nextauth].js

```
    ...
      pages: {
        signIn: '/auth/signin',
        signOut: '/auth/signout',
        error: '/auth/error', // Error code passed in query string as ?error=
        verifyRequest: '/auth/verify-request', // (used for check email message)
        newUser: null // If set, new users will be directed here on first sign in
      }
    ...

```

## Error codes[​](https://next-auth.js.org/v3/configuration/pages#error-codes "Direct link to heading")

보안 강화를 위해 반환되는 오류 코드를 의도적으로 제한합니다.

### Error page[​](https://next-auth.js.org/v3/configuration/pages#error-page "Direct link to heading")

다음 오류들은 기본 또는 재정의된 오류 페이지로 error 쿼리 파라미터로 전달됩니다:

- **Configuration** : 서버 구성에 문제가 있습니다. [options](https://next-auth.js.org/configuration/options#options)가 올바른지 확인하세요.
- **AccessDenied** : 보통 [`signIn` callback](https://next-auth.js.org/configuration/callbacks#sign-in-callback) 또는 [`redirect` callback](https://next-auth.js.org/configuration/callbacks#redirect-callback)을 통해 접근을 제한했을 때 발생합니다.
- **Verification** : Email provider와 관련됩니다. 토큰이 만료되었거나 이미 사용되었습니다.
- **Default** : 전체 예외 처리용이며, 위 항목들 중 어느 것도 일치하지 않을 때 적용됩니다.

예시: `/auth/error?error=Configuration`

### Sign-in page[​](https://next-auth.js.org/v3/configuration/pages#sign-in-page "Direct link to heading")

다음 오류들은 기본 또는 재정의된 로그인 페이지로 error 쿼리 파라미터로 전달됩니다:

- **OAuthSignin** : 인증 URL 구성 중 오류 발생 ([1](https://github.com/nextauthjs/next-auth/blob/457952bb5abf08b09861b0e5da403080cd5525be/src/server/lib/signin/oauth.js), [2](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/server/lib/oauth/pkce-handler.js), [3](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/server/lib/oauth/state-handler.js))
- **OAuthCallback** : OAuth provider의 응답 처리 중 오류 발생 ([1](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/server/lib/oauth/callback.js), [2](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/server/lib/oauth/pkce-handler.js), [3](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/server/lib/oauth/state-handler.js))
- **OAuthCreateAccount** : 데이터베이스에 OAuth provider 사용자를 생성할 수 없습니다.
- **EmailCreateAccount** : 데이터베이스에 email provider 사용자를 생성할 수 없습니다.
- **Callback** : [OAuth callback handler route](https://github.com/nextauthjs/next-auth/blob/main/src/server/routes/callback.js)에서 오류 발생
- **OAuthAccountNotLinked** : 계정의 이메일이 이미 연결되어 있지만, 현재 OAuth 계정과는 연결되어 있지 않은 경우
- **EmailSignin** : verification token이 포함된 e-mail 전송 실패
- **CredentialsSignin** : [Credentials provider](https://next-auth.js.org/providers/credentials)에서 `authorize` callback이 `null`을 반환했습니다. 자격 증명의 어느 부분이 잘못되었는지에 대한 정보를 제공하는 것은 악의적인 해커에게 악용될 수 있으므로 권장하지 않습니다.
- **Default** : 전체 예외 처리용이며, 위 항목들 중 어느 것도 일치하지 않을 때 적용됩니다.

예시: `/auth/error?error=Default`

## Theming[​](https://next-auth.js.org/v3/configuration/pages#theming "Direct link to heading")

기본적으로 내장 페이지는 [`prefer-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) Media Query를 활용해 시스템 테마를 따릅니다. [`theme` option](https://next-auth.js.org/configuration/options#theme)을 통해 이를 재정의하여 항상 다크 또는 라이트 테마를 사용하도록 할 수 있습니다.

## Examples[​](https://next-auth.js.org/v3/configuration/pages#examples "Direct link to heading")

### OAuth Sign in[​](https://next-auth.js.org/v3/configuration/pages#oauth-sign-in "Direct link to heading")

사용 가능한 인증 provider와 각 provider에 사용할 URL을 얻으려면 API endpoint `/api/auth/providers`로 요청을 보낼 수 있습니다:

pages/auth/signin.js

```
    import { getProviders, signIn } from "next-auth/client"

    export default function SignIn({ providers }) {
      return (
        <>
          {Object.values(providers).map((provider) => (
              <button onClick={() => signIn(provider.id)}>
                Sign in with {provider.name}
              </button>
          ))}
        </>
      )
    }

    // This is the recommended way for Next.js 9.3 or newer
    export async function getServerSideProps(context) {
      const providers = await getProviders()
      return {
        props: { providers },
      }
    }

    /*
    // If older than Next.js 9.3
    SignIn.getInitialProps = async () => {
      return {
        providers: await getProviders()
      }
    }
    */

```

### Email Sign in[​](https://next-auth.js.org/v3/configuration/pages#email-sign-in "Direct link to heading")

email 로그인용 커스텀 로그인 폼을 만들면, **email** 주소와 **/api/auth/csrf**의 **csrfToken** 두 필드를 모두 **/api/auth/signin/email**로 보내는 POST 요청에 포함해야 합니다.

pages/auth/email-signin.js

```
    import { getCsrfToken } from "next-auth/client"

    export default function SignIn({ csrfToken }) {
      return (
        <form method="post" action="/api/auth/signin/email">
          <input name="csrfToken" type="hidden" defaultValue={csrfToken} />
          <label>
            Email address
            <input type="email" id="email" name="email" />
          </label>
          <button type="submit">Sign in with Email</button>
        </form>
      )
    }

    // This is the recommended way for Next.js 9.3 or newer
    export async function getServerSideProps(context) {
      const csrfToken = await getCsrfToken(context)
      return {
        props: { csrfToken },
      }
    }

    /*
    // If older than Next.js 9.3
    SignIn.getInitialProps = async (context) => {
      return {
        csrfToken: await getCsrfToken(context)
      }
    }
    */

```

`signIn()` 함수를 사용해도 되며, 이 경우 CSRF token 획득을 자동으로 처리합니다:

```
    signIn("email", { email: "jsmith@example.com" })

```

### Credentials Sign in[​](https://next-auth.js.org/v3/configuration/pages#credentials-sign-in "Direct link to heading")

credentials 기반 인증용 로그인 폼을 만들면, **/api/auth/csrf**의 **csrfToken**을 **/api/auth/callback/credentials**로 보내는 POST 요청에 포함해야 합니다.

pages/auth/credentials-signin.js

```
    import { getCsrfToken } from "next-auth/client"

    export default function SignIn({ csrfToken }) {
      return (
        <form method="post" action="/api/auth/callback/credentials">
          <input name="csrfToken" type="hidden" defaultValue={csrfToken} />
          <label>
            Username
            <input name="username" type="text" />
          </label>
          <label>
            Password
            <input name="password" type="password" />
          </label>
          <button type="submit">Sign in</button>
        </form>
      )
    }

    // This is the recommended way for Next.js 9.3 or newer
    export async function getServerSideProps(context) {
      return {
        props: {
          csrfToken: await getCsrfToken(context),
        },
      }
    }

    /*
    // If older than Next.js 9.3
    SignIn.getInitialProps = async (context) => {
      return {
        csrfToken: await getCsrfToken(context)
      }
    }
    */

```

`signIn()` 함수를 사용해도 되며, 이 경우 CSRF token 획득을 자동으로 처리합니다:

```
    signIn("credentials", { username: "jsmith", password: "1234" })

```

tip

API 코드 전용인 **/pages/api** 외부 폴더에 커스텀 페이지를 두어야 한다는 점을 기억하세요. 위 예시처럼 권장되는 위치 관례는 `pages/auth/...`입니다.
