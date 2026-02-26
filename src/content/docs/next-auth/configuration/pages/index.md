---
title: '오류 코드[\u200b](https://next-auth.js.org/configuration/pages#error-codes "Direct link to heading")'
description: "NextAuth.js는 로그인, 로그아웃, 이메일 인증 처리 및 오류 메시지 표시를 위한 단순하고 브랜드가 적용되지 않은 인증 페이지를 자동으로 생성합니다."
---

Source URL: https://next-auth.js.org/configuration/pages

# 페이지 | NextAuth.js

버전: v4

NextAuth.js는 로그인, 로그아웃, 이메일 인증 처리 및 오류 메시지 표시를 위한 단순하고 브랜드가 적용되지 않은 인증 페이지를 자동으로 생성합니다.

회원가입 페이지에 표시되는 옵션은 NextAuth.js에 전달된 옵션에 지정된 provider를 기반으로 자동 생성됩니다.

커스텀 로그인 페이지를 추가하려면 `pages` 옵션을 사용할 수 있습니다:

pages/api/auth/[...nextauth].js

```
    ...
      pages: {
        signIn: '/auth/signin',
        signOut: '/auth/signout',
        error: '/auth/error', // Error code passed in query string as ?error=
        verifyRequest: '/auth/verify-request', // (used for check email message)
        newUser: '/auth/new-user' // New users will be directed here on first sign in (leave the property out if not of interest)
      }
    ...

```

note

이 구성을 사용할 때는 해당 페이지들이 실제로 존재하는지 확인하세요. 예를 들어 `error: '/auth/error'`는 `pages/auth/error.js`에 있는 페이지 파일을 가리킵니다.

## 오류 코드[​](https://next-auth.js.org/configuration/pages#error-codes "Direct link to heading")

보안 강화를 위해 반환되는 오류 코드를 의도적으로 제한합니다.

### 오류 페이지[​](https://next-auth.js.org/configuration/pages#error-page "Direct link to heading")

다음 오류들은 기본 또는 재정의된 오류 페이지로 error 쿼리 파라미터로 전달됩니다:

- **Configuration** : 서버 구성에 문제가 있습니다. [options](https://next-auth.js.org/configuration/options#options)가 올바른지 확인하세요.
- **AccessDenied** : 보통 [`signIn` callback](https://next-auth.js.org/configuration/callbacks#sign-in-callback) 또는 [`redirect` callback](https://next-auth.js.org/configuration/callbacks#redirect-callback)을 통해 접근을 제한했을 때 발생합니다.
- **Verification** : Email provider와 관련된 오류입니다. 토큰이 만료되었거나 이미 사용되었습니다.
- **Default** : 포괄 처리용이며, 위 항목 중 어느 것도 일치하지 않을 때 적용됩니다.

예시: `/auth/error?error=Configuration`

### 로그인 페이지[​](https://next-auth.js.org/configuration/pages#sign-in-page "Direct link to heading")

다음 오류들은 기본 또는 재정의된 로그인 페이지로 error 쿼리 파라미터로 전달됩니다:

- **OAuthSignin** : 인증 URL 구성 중 오류 ([1](https://github.com/nextauthjs/next-auth/blob/457952bb5abf08b09861b0e5da403080cd5525be/src/server/lib/signin/oauth.js), [2](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/core/lib/oauth/pkce-handler.ts), [3](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/core/lib/oauth/state-handler.ts)),
- **OAuthCallback** : OAuth provider의 응답을 처리하는 과정에서 오류 ([1](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/core/lib/oauth/callback.ts), [2](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/core/lib/oauth/pkce-handler.ts), [3](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/core/lib/oauth/state-handler.ts)).
- **OAuthCreateAccount** : 데이터베이스에 OAuth provider 사용자를 생성할 수 없습니다.
- **EmailCreateAccount** : 데이터베이스에 email provider 사용자를 생성할 수 없습니다.
- **Callback** : [OAuth callback handler route](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/core/routes/callback.ts)에서 발생한 오류
- **OAuthAccountNotLinked** : 계정의 이메일은 이미 연결되어 있지만, 이 OAuth 계정과는 연결되어 있지 않은 경우
- **EmailSignin** : 인증 토큰이 포함된 e-mail 전송 실패
- **CredentialsSignin** : [Credentials provider](https://next-auth.js.org/providers/credentials)에서 `authorize` callback이 `null`을 반환했습니다. 자격 증명의 어느 부분이 잘못되었는지에 대한 정보를 제공하는 것은 악의적인 해커에게 악용될 수 있으므로 권장하지 않습니다.
- **SessionRequired** : 이 페이지의 콘텐츠는 항상 로그인 상태여야 합니다. 구성 방법은 [useSession](https://next-auth.js.org/getting-started/client#require-session)을 참고하세요.
- **Default** : 포괄 처리용이며, 위 항목 중 어느 것도 일치하지 않을 때 적용됩니다.

예시: `/auth/signin?error=Default`

## 테마[​](https://next-auth.js.org/configuration/pages#theming "Direct link to heading")

기본적으로 내장 페이지는 [`prefer-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) Media Query를 사용해 시스템 테마를 따릅니다. [`theme.colorScheme` option](https://next-auth.js.org/configuration/options#theme)을 통해 이를 재정의하여 항상 다크 또는 라이트 테마를 사용할 수 있습니다.

또한 `theme.brandColor`를 정의해 내장 페이지의 커스텀 강조 색상을 지정할 수 있습니다. `theme.logo`에 로고 URL을 지정하면 해당 페이지의 기본 카드 상단에 렌더링됩니다.

#### 로그인[​](https://next-auth.js.org/configuration/pages#sign-in "Direct link to heading")

![커스터마이즈된 로그인 페이지](https://next-auth.js.org/assets/images/pages_signin-940a5db521096f0bace59b44ecfd78b1.png)

#### 로그아웃[​](https://next-auth.js.org/configuration/pages#sign-out "Direct link to heading")

![커스터마이즈된 로그아웃 페이지](https://next-auth.js.org/assets/images/pages_signout-0d202813326a52aa99579ce9894b9064.png)

## 예제[​](https://next-auth.js.org/configuration/pages#examples "Direct link to heading")

### OAuth 로그인[​](https://next-auth.js.org/configuration/pages#oauth-sign-in "Direct link to heading")

사용 가능한 인증 provider와 각 URL을 얻으려면 API endpoint `/api/auth/providers`로 요청할 수 있습니다:

pages/auth/signin.tsx

```
    import type {
      GetServerSidePropsContext,
      InferGetServerSidePropsType,
    } from "next"
    import { getProviders, signIn } from "next-auth/react"
    import { getServerSession } from "next-auth/next"
    import { authOptions } from "../api/auth/[...nextauth]"

    export default function SignIn({
      providers,
    }: InferGetServerSidePropsType<typeof getServerSideProps>) {
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

    export async function getServerSideProps(context: GetServerSidePropsContext) {
      const session = await getServerSession(context.req, context.res, authOptions)

      // If the user is already logged in, redirect.
      // Note: Make sure not to redirect to the same page
      // To avoid an infinite loop!
      if (session) {
        return { redirect: { destination: "/" } }
      }

      const providers = await getProviders()

      return {
        props: { providers: providers ?? [] },
      }
    }

```

더 완전한 스타일이 적용된 로그인 페이지 예제는 [여기](https://github.com/ndom91/next-auth-example-sign-in-page)에서 확인할 수 있습니다.

### Email 로그인[​](https://next-auth.js.org/configuration/pages#email-sign-in "Direct link to heading")

Email 로그인용 커스텀 로그인 폼을 만들 경우, **email** 주소와 **/api/auth/csrf**의 **csrfToken** 두 필드를 모두 **/api/auth/signin/email**로 보내는 POST 요청에 포함해야 합니다.

pages/auth/email-signin.tsx

```
    import type {
      GetServerSidePropsContext,
      InferGetServerSidePropsType,
    } from "next"
    import { getCsrfToken } from "next-auth/react"

    export default function SignIn({
      csrfToken,
    }: InferGetServerSidePropsType<typeof getServerSideProps>) {
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

    export async function getServerSideProps(context: GetServerSidePropsContext) {
      const csrfToken = await getCsrfToken(context)
      return {
        props: { csrfToken },
      }
    }

```

`signIn()` 함수를 사용할 수도 있으며, 이 경우 CSRF 토큰을 자동으로 가져옵니다:

```
    signIn("email", { email: "jsmith@example.com" })

```

### Credentials 로그인[​](https://next-auth.js.org/configuration/pages#credentials-sign-in "Direct link to heading")

Credentials 기반 인증용 로그인 폼을 만들 경우, **/api/auth/csrf**의 **csrfToken**을 **/api/auth/callback/credentials**로 보내는 POST 요청에 포함해야 합니다.

pages/auth/credentials-signin.tsx

```
    import type {
      GetServerSidePropsContext,
      InferGetServerSidePropsType,
    } from "next"
    import { getCsrfToken } from "next-auth/react"

    export default function SignIn({
      csrfToken,
    }: InferGetServerSidePropsType<typeof getServerSideProps>) {
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

    export async function getServerSideProps(context: GetServerSidePropsContext) {
      return {
        props: {
          csrfToken: await getCsrfToken(context),
        },
      }
    }

```

`signIn()` 함수를 사용할 수도 있으며, 이 경우 CSRF 토큰을 자동으로 가져옵니다:

```
    signIn("credentials", { username: "jsmith", password: "1234" })

```

tip

커스텀 페이지는 API 코드 전용인 **/pages/api** 밖의 폴더에 두어야 한다는 점을 기억하세요. 위 예시처럼 위치 규칙으로 `pages/auth/...`를 권장합니다.
